import os,io,hashlib,gzip,shutil,time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
from pandas.tseries.offsets import BDay
from threading import Thread


from SharedData.Logger import Logger
from SharedData.SharedDataFrame import SharedDataFrame
from SharedData.SharedDataTimeSeries import SharedDataTimeSeries
from SharedData.SharedDataAWSS3 import S3Upload,S3Download,UpdateModTime

class SharedDataPeriod:

    def __init__(self, sharedDataFeeder, period):
        self.sharedDataFeeder = sharedDataFeeder        
        self.sharedData = sharedDataFeeder.sharedData        
        self.period = period
            
        # DATA DICTIONARY
        # tags[tag]
        self.tags = {}        

        # TIME INDEX
        self.timeidx = {}
        self.ctimeidx = {}        
        if self.period=='W1':
            self.periodSeconds = 7*60*60*24
            self.default_startDate = pd.Timestamp('1990-01-01')
        elif self.period=='D1':
            self.periodSeconds = 60*60*24       
            self.default_startDate = pd.Timestamp('1990-01-01')
        elif self.period=='M15':
            self.periodSeconds = 60*15
            self.default_startDate = pd.Timestamp('1990-01-01')
        elif self.period=='M1':
            self.periodSeconds = 60
            self.default_startDate = pd.Timestamp('2010-01-01')
        self.getContinousTimeIndex(self.default_startDate)
        self.loaded = False

    def load(self):
        # read if not loaded
        shdatalist = self.sharedData.list()   
        path, shm_name = self.get_path()
        idx = [shm_name in str(s) for s in shdatalist.index]
        if not np.any(idx):
            self.read()
        else:
            #map
            self.map(shm_name,shdatalist.index[idx])

    def __setitem__(self, tag, df):
        if not tag in self.tags.keys():
            if isinstance(tag, pd.Timestamp):
                self.tags[tag] = SharedDataFrame(self, tag, df)
            else:
                self.tags[tag] = SharedDataTimeSeries(self, tag, df)
        elif isinstance(df, pd.DataFrame):
            data = self.tags[tag].data
            iidx = df.index.intersection(data.index)
            icol = df.columns.intersection(data.columns)
            data.loc[iidx, icol] = df.loc[iidx, icol].copy()

    def __getitem__(self, tag):     
        if not self.loaded:
            self.load()
            self.loaded=True
        if not tag in self.tags.keys():
            if isinstance(tag, pd.Timestamp):
                df = SharedDataFrame(self, tag)
                if not df.data.empty:
                    self.tags[tag] = df
                else:
                    return pd.DataFrame([])
            else:                
                ts = SharedDataTimeSeries(self, tag)                
                if not ts.data.empty:
                    self.tags[tag] = ts
                else:
                    return pd.DataFrame([])
        return self.tags[tag].data

    def getTimeIndex(self, startDate):
        if not startDate in self.timeidx.keys():
            nextsaturday = datetime.today() + BDay(21)\
                + timedelta((12 - datetime.today().weekday()) % 7)
                        
            if self.period=='D1':
                self.timeidx[startDate] = pd.Index(\
                    pd.bdate_range(start=startDate,\
                    end=np.datetime64(nextsaturday)))
                self.periodSeconds = 60*60*24
            
            elif self.period=='M15':
                self.timeidx[startDate] = pd.Index(\
                    pd.bdate_range(start=startDate,\
                    end=np.datetime64(nextsaturday),freq='15min'))                    
                idx = (self.timeidx[startDate].hour>8) 
                idx = (idx) & (self.timeidx[startDate].hour<19)
                idx = (idx) & (self.timeidx[startDate].day_of_week<5)
                self.timeidx[startDate] = self.timeidx[startDate][idx]
                self.periodSeconds = 60*15

            elif self.period=='M1':
                self.timeidx[startDate] = pd.Index(\
                    pd.bdate_range(start=startDate,\
                    end=np.datetime64(nextsaturday),freq='1min'))                    
                idx = (self.timeidx[startDate].hour>8) 
                idx = (idx) & (self.timeidx[startDate].hour<19)
                idx = (idx) & (self.timeidx[startDate].day_of_week<5)
                self.timeidx[startDate] = self.timeidx[startDate][idx]
                self.periodSeconds = 60
                
        return self.timeidx[startDate]
                
    def getContinousTimeIndex(self, startDate):
        if not startDate in self.ctimeidx.keys():            
            _timeidx = self.getTimeIndex(startDate)
            nsec = (_timeidx - startDate).astype(np.int64)
            periods = (nsec/(10**9)/self.periodSeconds).astype(np.int64)
            self.ctimeidx[startDate] = np.empty(max(periods)+1)
            self.ctimeidx[startDate][:] = np.nan
            self.ctimeidx[startDate][periods.values] = np.arange(len(periods))        
        return self.ctimeidx[startDate]

    def get_path(self):        
        shm_name = self.sharedData.user + '/' + self.sharedData.database + '/' \
            + self.sharedDataFeeder.feeder + '/' + self.period
        if os.name=='posix':
            shm_name = shm_name.replace('/','\\')

        path = Path(os.environ['DATABASE_FOLDER'])
        path = path / self.sharedData.user
        path = path / self.sharedData.database
        path = path / self.sharedDataFeeder.feeder
        path = path / self.period
        path = Path(str(path).replace('\\','/'))
        if self.sharedData.save_local:
            if not os.path.isdir(path.parent):
                os.makedirs(path.parent)
        return path , shm_name

    #CREATE
    def create_timeseries(self,tag,startDate,columns,overwrite=False):
        self.tags[tag] = SharedDataTimeSeries(\
            self,tag,startDate=startDate,columns=columns,overwrite=overwrite)
        return self.tags[tag].data

    # READ
    def map(self,shm_name,shm_name_list):
        for shm in shm_name_list:
            tag = shm.replace(shm_name,'')[1:]
            self.tags[tag] = SharedDataTimeSeries(self, tag = tag)            


    def read(self):
        tini = time.time()
        datasize = 1
        path, shm_name= self.get_path()
        headpath = str(path)+'_head.bin'
        tailpath = str(path)+'_tail.bin'        
        head_io = None
        tail_io = None
        if self.sharedData.s3read:
            force_download= (not self.sharedData.save_local)
            
            [head_io_gzip, head_local_mtime, head_remote_mtime] = \
                S3Download(str(headpath),str(headpath)+'.gzip',force_download)
            if not head_io_gzip is None:
                head_io = io.BytesIO()
                head_io_gzip.seek(0)
                with gzip.GzipFile(fileobj=head_io_gzip, mode='rb') as gz:
                    shutil.copyfileobj(gz,head_io)
                if self.sharedData.save_local:
                    SharedDataPeriod.write_file(head_io,headpath,mtime=head_remote_mtime)
                    UpdateModTime(headpath,head_remote_mtime)
                    
            
            [tail_io_gzip, tail_local_mtime, tail_remote_mtime] = \
                S3Download(str(tailpath),str(tailpath)+'.gzip',force_download)
            if not tail_io_gzip is None:
                tail_io = io.BytesIO()
                tail_io_gzip.seek(0)
                with gzip.GzipFile(fileobj=tail_io_gzip, mode='rb') as gz:
                    shutil.copyfileobj(gz,tail_io)
                if self.sharedData.save_local:
                    SharedDataPeriod.write_file(tail_io,tailpath,mtime=tail_remote_mtime)
                    UpdateModTime(tailpath,tail_remote_mtime)

        if (head_io is None) & (self.sharedData.save_local):
            # read local
            if os.path.isfile(str(headpath)):
                head_io = open(str(headpath),'rb')            
            
        if (tail_io is None) & (self.sharedData.save_local):
            if os.path.isfile(str(tailpath)):
                tail_io = open(str(tailpath),'rb')

        if not head_io is None:
            datasize += self.read_io(head_io,headpath)

        if not tail_io is None:
            datasize += self.read_io(tail_io,tailpath)

        te = time.time()-tini+0.000001   
        datasize = datasize/(1024*1024)
        Logger.log.debug('read %s/%s %.2fMB in %.2fs %.2fMBps ' % \
            (self.sharedDataFeeder,self.period,datasize,te,datasize/te))

    def read_io(self,io_obj,path):
        datasize = 0        
        #read
        io_obj.seek(0)
        io_data = io_obj.read()
        datasize = len(io_data)
        _m = hashlib.md5(io_data[:-24]).digest()
        m = io_data[-16:]
        if (m!=_m):
            Logger.log.error('Timeseries read_head() file %s corrupted!' % (path))
            raise Exception('Timeseries read_head() %s corrupted!' % (path))
        io_obj.seek(0)
        separator = np.frombuffer(io_obj.read(8),dtype=np.int64)[0]        
        while (separator==1):
            _header = np.frombuffer(io_obj.read(40),dtype=np.int64)
            _tag_b = io_obj.read(int(_header[0]))
            _tag = _tag_b.decode(encoding='UTF-8',errors='ignore')
            _idx_b = io_obj.read(int(_header[1]))
            _idx = pd.to_datetime(np.frombuffer(_idx_b,dtype=np.int64))
            _colscsv_b = io_obj.read(int(_header[2]))
            _colscsv = _colscsv_b.decode(encoding='UTF-8',errors='ignore')
            _cols = _colscsv.split(',')
            r = _header[3]
            c = _header[4]
            total_bytes = int(r*c*8)
            _data = np.frombuffer(io_obj.read(total_bytes),dtype=np.float64).reshape((r,c))
            df = pd.DataFrame(_data,index=_idx,columns=_cols)
            if not _tag in self.tags.keys():
                self.tags[_tag] = SharedDataTimeSeries(self, tag = _tag, value = df)
            else:
                data = self.tags[_tag].data
                iidx = df.index.intersection(data.index)
                icol = df.columns.intersection(data.columns)
                data.loc[iidx, icol] = df.loc[iidx, icol].copy()
            separator = np.frombuffer(io_obj.read(8),dtype=np.int64)[0]
        io_obj.close()

        return datasize

    # WRITE
    def write(self,startDate=None):
        path , shm_name= self.get_path()                
        mtime = datetime.now().timestamp()
        partdate = pd.Timestamp(datetime(datetime.now().year,1,1))
        firstdate = pd.Timestamp('1970-01-01')
        if not startDate is None:
            firstdate = startDate        
        if firstdate<partdate:
            self.write_head(path,partdate,mtime)
        
        self.write_tail(path,partdate,mtime)

    def write_head(self,path,partdate,mtime):
        io_obj = self.create_head_io(partdate)
        
        threads=[]
        if self.sharedData.s3write:
            io_obj.seek(0)
            gzip_io = io.BytesIO()
            with gzip.GzipFile(fileobj=gzip_io, mode='wb', compresslevel=1) as gz:
                shutil.copyfileobj(io_obj, gz)            
            threads = [*threads , Thread(target=S3Upload,\
                args=(gzip_io, str(path)+'_head.bin.gzip', mtime) )]

        if self.sharedData.save_local:
            threads = [*threads , Thread(target=SharedDataPeriod.write_file, \
                args=(io_obj, str(path)+'_head.bin', mtime) )]
        
        for i in range(len(threads)):
            threads[i].start()

        for i in range(len(threads)):
            threads[i].join()         

    def create_head_io(self,partdate):
        io_obj = io.BytesIO()
        for tag in self.tags.keys():
            dftag = self[tag].loc[:partdate]
            startdate = dftag.index[0]
            #create binary df    
            df = dftag.dropna(how='all',axis=0).copy()
            # insert first line to maintain startdate
            df.loc[startdate,:] = dftag.loc[startdate,:]
            r, c = df.shape
            tag_b = str.encode(tag,encoding='UTF-8',errors='ignore')
            idx = (df.index.astype(np.int64))
            idx_b = idx.values.tobytes()
            cols = df.columns.values
            colscsv = ','.join(cols)
            colscsv_b = str.encode(colscsv,encoding='UTF-8',errors='ignore')
            nbtag = len(tag_b)
            nbidx = len(idx_b)
            nbcols = len(colscsv_b)        
            header = np.array([1,nbtag,nbidx,nbcols,r,c]).astype(np.int64)
            io_obj.write(header)
            io_obj.write(tag_b)
            io_obj.write(idx_b)
            io_obj.write(colscsv_b)
            io_obj.write(np.ascontiguousarray(df.values.astype(np.float64)))

        m = hashlib.md5(io_obj.getvalue()).digest()
        io_obj.write(np.array([0]).astype(int))
        io_obj.write(m)
        return io_obj

    def write_tail(self,path,partdate,mtime):
        io_obj = self.create_tail_io(partdate)
        
        threads=[]
        if self.sharedData.s3write:
            io_obj.seek(0)
            gzip_io = io.BytesIO()
            with gzip.GzipFile(fileobj=gzip_io, mode='wb', compresslevel=1) as gz:
                shutil.copyfileobj(io_obj, gz)            
            threads = [*threads , Thread(target=S3Upload,\
                args=(gzip_io, str(path)+'_tail.bin.gzip', mtime) )]

        if self.sharedData.save_local:
            threads = [*threads , Thread(target=SharedDataPeriod.write_file, \
                args=(io_obj, str(path)+'_tail.bin', mtime) )]
        
        for i in range(len(threads)):
            threads[i].start()

        for i in range(len(threads)):
            threads[i].join()         

    def create_tail_io(self,partdate):
        io_obj = io.BytesIO()
        for tag in self.tags.keys():
            dftag = self[tag].loc[partdate:]
            #create binary df    
            df = dftag.dropna(how='all',axis=0)            
            r, c = df.shape
            tag_b = str.encode(tag,encoding='UTF-8',errors='ignore')
            idx = (df.index.astype(np.int64))
            idx_b = idx.values.tobytes()
            cols = df.columns.values
            colscsv = ','.join(cols)
            colscsv_b = str.encode(colscsv,encoding='UTF-8',errors='ignore')
            nbtag = len(tag_b)
            nbidx = len(idx_b)
            nbcols = len(colscsv_b)        
            header = np.array([1,nbtag,nbidx,nbcols,r,c]).astype(np.int64)
            io_obj.write(header)
            io_obj.write(tag_b)
            io_obj.write(idx_b)
            io_obj.write(colscsv_b)
            io_obj.write(np.ascontiguousarray(df.values.astype(np.float64)))

        m = hashlib.md5(io_obj.getvalue()).digest()
        io_obj.write(np.array([0]).astype(int))
        io_obj.write(m)
        return io_obj

    def write_file(io_obj,path,mtime):
        with open(path, 'wb') as f:
            f.write(io_obj.getbuffer())
            f.flush()
        os.utime(path, (mtime, mtime))