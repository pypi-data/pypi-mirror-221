# THIRD PARTY LIBS
import os,sys
import pandas as pd
import numpy as np
import json
import time
from numba import jit
from pathlib import Path
from multiprocessing import shared_memory
import io, gzip, hashlib, shutil
from threading import Thread

from subprocess import run, PIPE
from datetime import datetime, timedelta

from SharedData.Logger import Logger
from SharedData.SharedDataAWSS3 import S3Upload,S3Download,UpdateModTime
from SharedData.SharedDataRealTime import SharedDataRealTime

class SharedDataTimeSeries:

    def __init__(self, sharedDataPeriod, tag, value=None,\
            startDate=None,columns=None,overwrite=False):
        self.sharedDataPeriod = sharedDataPeriod
        self.tag = tag
        
        self.sharedDataFeeder = sharedDataPeriod.sharedDataFeeder
        self.sharedData = sharedDataPeriod.sharedDataFeeder.sharedData        

        self.period = sharedDataPeriod.period
        self.periodSeconds = sharedDataPeriod.periodSeconds               
        self.feeder = self.sharedDataFeeder.feeder

        # test if shared memory already exists        
        if self.ismalloc():            
            self.create_map = 'map'
        else:
            self.create_map = 'create'

        self.init_time = time.time()
        self.download_time = pd.NaT
        self.last_update = pd.NaT
        self.first_update = pd.NaT
        
        # Time series dataframe
        self.data = pd.DataFrame()
        self.index = pd.Index([])
        self.columns = pd.Index([])

        # initalize
        try:
            if ((self.create_map == 'create') | (overwrite)):
                if (not startDate is None):
                    # create new empty shared memory
                    self.startDate = startDate
                    self.columns = columns
                    self.malloc_create()

                elif (not value is None):
                    # allocate existing data
                    self.startDate = value.index[0]                    
                    self.columns = value.columns  
                    self.malloc_create()
                    sidx = np.array([self.get_loc_symbol(s) for s in self.columns])
                    ts = value.index.values.astype(np.int64)/10**9 #seconds
                    tidx = self.get_loc_timestamp(ts)
                    self.setValuesJit(self.data.values,tidx,sidx,value.values)

                elif (value is None):                    
                    # read & allocate data
                    tini = time.time()
                    datasize = self.read()
                    datasize /= (1024*1024)
                    te = time.time()-tini+0.000001                    
                    Logger.log.debug('read %s/%s %.2fMB in %.2fs %.2fMBps ' % \
                        (self.feeder,self.tag,datasize,te,datasize/te))
                    
            elif (self.create_map == 'map'):
                # map existing shared memory
                self.malloc_map()
                if (not value is None):
                    Logger.log.warning('Tag %s exists in memory setting values '\
                                       'but index and columns may differ!' % tag)
                    iidx = value.index.intersection(self.data.index)
                    icol = value.columns.intersection(self.data.columns)
                    self.data.loc[iidx,icol] = value.loc[iidx,icol].copy()
        except Exception as e:
            path, shm_name = self.get_path()
            Logger.log.error('Error initalizing %s!\n%s' % (shm_name,str(e)))
            self.free()
            
        self.init_time = time.time() - self.init_time

    def get_path(self):
        shm_name = self.sharedData.user + '/' + self.sharedData.database + '/' \
            + self.sharedDataFeeder.feeder + '/' + self.period + '/' + self.tag
        if os.name=='posix':
            shm_name = shm_name.replace('/','\\')
            
        path = Path(os.environ['DATABASE_FOLDER'])
        path = path / self.sharedData.user
        path = path / self.sharedData.database
        path = path / self.sharedDataFeeder.feeder
        path = path / self.period
        path = path / self.tag
        path = Path(str(path).replace('\\','/'))
        if self.sharedData.save_local:
            if not os.path.isdir(path):
                os.makedirs(path)
        
        return path, shm_name

    def ismalloc(self):
        path, shm_name = self.get_path()
        [self.shm, ismalloc] = self.sharedData.malloc(shm_name)
        return ismalloc

    def malloc_create(self):
        path, shm_name = self.get_path()
        self.symbolidx = {}
        for i in range(len(self.columns)):
            self.symbolidx[self.columns.values[i]] = i
        self.index = self.sharedDataPeriod.getTimeIndex(self.startDate)
        self.ctimeidx = self.sharedDataPeriod.getContinousTimeIndex(self.startDate)
        try: # try create memory file
            r = len(self.index)
            c = len(self.columns)
                        
            idx_b = self.index.astype(np.int64).values.tobytes()
            colscsv_b = str.encode(','.join(self.columns.values),\
                encoding='UTF-8',errors='ignore')
            nb_idx = len(idx_b)
            nb_cols = len(colscsv_b)
            nb_data = int(r*c*8)
            header_b = np.array([r,c,nb_idx,nb_cols,nb_data]).astype(np.int64).tobytes()
            nb_header = len(header_b)
            
            nb_buf = nb_header+nb_idx+nb_cols+nb_data
            nb_offset = nb_header+nb_idx+nb_cols

            [self.shm, ismalloc] = self.sharedData.malloc(shm_name,create=True,size=nb_buf)
            
            i=0
            self.shm.buf[i:nb_header] = header_b
            i = i + nb_header
            self.shm.buf[i:i+nb_idx] = idx_b
            i = i + nb_idx
            self.shm.buf[i:i+nb_cols] = colscsv_b

            self.shmarr = np.ndarray((r,c),\
                dtype=np.float64, buffer=self.shm.buf, offset=nb_offset)
            
            self.shmarr[:] = np.nan
            
            self.data = pd.DataFrame(self.shmarr,\
                        index=self.index,\
                        columns=self.columns,\
                        copy=False)
                        
            return True
        except Exception as e:
            Logger.log.error('Failed to malloc_create\n%s' % str(e))
            return False

    def malloc_map(self):
        try: # try map memory file
            path, shm_name = self.get_path()        
            [self.shm, ismalloc] = self.sharedData.malloc(shm_name)
            
            i=0
            nb_header=40
            header = np.frombuffer(self.shm.buf[i:nb_header],dtype=np.int64)
            i = i + nb_header
            nb_idx = header[2]
            idx_b = bytes(self.shm.buf[i:i+nb_idx])
            self.index = pd.to_datetime(np.frombuffer(idx_b,dtype=np.int64))
            i = i + nb_idx
            nb_cols = header[3]
            cols_b = bytes(self.shm.buf[i:i+nb_cols])
            self.columns = cols_b.decode(encoding='UTF-8',errors='ignore').split(',')

            r = header[0]
            c = header[1]        
            nb_data = header[4]
            nb_offset = nb_header+nb_idx+nb_cols                
            
            self.shmarr = np.ndarray((r,c), dtype=np.float64,\
                buffer=self.shm.buf, offset=nb_offset)

            self.data = pd.DataFrame(self.shmarr,\
                        index=self.index,\
                        columns=self.columns,\
                        copy=False)
        
            return True
        except Exception as e:
            Logger.log.error('Failed to malloc_map\n%s' % str(e))
            return False

    # READ
    def read(self):           
        datasize = 1
        path, shm_name = self.get_path()
        headpath = path / (self.tag+'_head.bin')
        tailpath = path / (self.tag+'_tail.bin')   
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
                    SharedDataTimeSeries.write_file(head_io,headpath,mtime=head_remote_mtime)
                    UpdateModTime(headpath,head_remote_mtime)
                    
            
            [tail_io_gzip, tail_local_mtime, tail_remote_mtime] = \
                S3Download(str(tailpath),str(tailpath)+'.gzip',force_download)
            if not tail_io_gzip is None:
                tail_io = io.BytesIO()
                tail_io_gzip.seek(0)
                with gzip.GzipFile(fileobj=tail_io_gzip, mode='rb') as gz:
                    shutil.copyfileobj(gz,tail_io)
                if self.sharedData.save_local:
                    SharedDataTimeSeries.write_file(tail_io,tailpath,mtime=tail_remote_mtime)
                    UpdateModTime(tailpath,tail_remote_mtime)
        
        if (head_io is None) & (self.sharedData.save_local):
            # read local
            if os.path.isfile(str(headpath)):
                head_io = open(str(headpath),'rb')
            
        if (tail_io is None) & (self.sharedData.save_local):
            if os.path.isfile(str(tailpath)):
                tail_io = open(str(tailpath),'rb')
        
        self.startDate = None
        self.columns = pd.Index([])
        # read index, columns        
        if not head_io is None:
            head_io.seek(0)
            [index,columns] = self.read_header(head_io)
            self.columns = self.columns.union(columns)
            self.startDate = pd.Timestamp(index.values[0])

        if not tail_io is None:
            tail_io.seek(0)
            [index,columns] = self.read_header(tail_io)
            self.columns = self.columns.union(columns)            
            if self.startDate==None:
                self.startDate = pd.Timestamp(index.values[0])
        
        if not self.startDate is None:
            self.malloc_create()
            # read data
            if not head_io is None:
                head_io.seek(0)                
                datasize+=self.read_data(head_io,headpath)                
                head_io.close()

            if not tail_io is None:
                tail_io.seek(0)                
                datasize+=self.read_data(tail_io,tailpath)
                tail_io.close()
        
        return datasize

    def read_header(self,data_io):
        _header = np.frombuffer(data_io.read(40),dtype=np.int64)
        _idx_b = data_io.read(int(_header[2]))
        _idx = pd.to_datetime(np.frombuffer(_idx_b,dtype=np.int64))
        _colscsv_b = data_io.read(int(_header[3]))
        _colscsv = _colscsv_b.decode(encoding='UTF-8',errors='ignore')
        _cols = _colscsv.split(',')
        return [_idx,_cols]

    def read_data(self,data_io,path):
        _header = np.frombuffer(data_io.read(40),dtype=np.int64)
        _idx_b = data_io.read(int(_header[2]))
        _idx = pd.to_datetime(np.frombuffer(_idx_b,dtype=np.int64))
        _colscsv_b = data_io.read(int(_header[3]))
        _colscsv = _colscsv_b.decode(encoding='UTF-8',errors='ignore')
        _cols = _colscsv.split(',')
        _data = np.frombuffer(data_io.read(int(_header[4])),dtype=np.float64).reshape((_header[0],_header[1]))
        #calculate hash
        _m = hashlib.md5(_idx_b)
        _m.update(_colscsv_b)
        _m.update(_data)
        _md5hash_b = _m.digest()
        __md5hash_b = data_io.read(16)
        if not _md5hash_b==__md5hash_b:
            raise Exception('Timeseries file corrupted!\n%s' % (path))
        sidx = np.array([self.get_loc_symbol(s) for s in _cols])
        ts = _idx.values.astype(np.int64)/10**9 #seconds
        tidx = self.get_loc_timestamp(ts)
        self.setValuesJit(self.data.values,tidx,sidx,_data)
        data_io.close()
        return _header[4]
 
    # WRITE
    def write(self, startDate=None):
        firstdate = self.data.first_valid_index()
        if not startDate is None:
            firstdate = startDate
        
        path, shm_name = self.get_path()
        
        partdate = pd.Timestamp(datetime(datetime.now().year,1,1))
        threads = []

        mtime = datetime.now().timestamp()        
        if firstdate<partdate:
            # write head
            threads = [*threads , \
                Thread(target=SharedDataTimeSeries.write_timeseries_df,\
                    args=(self,self.data.loc[:partdate], str(path / (self.tag+'_head.bin')), mtime) )]
        # write tail
        threads = [*threads , \
                Thread(target=SharedDataTimeSeries.write_timeseries_df,\
                    args=(self,self.data.loc[partdate:], str(path / (self.tag+'_tail.bin')), mtime) )]

        for i in range(len(threads)):
            threads[i].start()

        for i in range(len(threads)):
            threads[i].join()
        
    def write_timeseries_df(self,df,tag_path,mtime):
        ts_io = SharedDataTimeSeries.create_timeseries_io(df)        
        threads=[]
        if self.sharedData.s3write:
            ts_io.seek(0)
            gzip_io = io.BytesIO()
            with gzip.GzipFile(fileobj=gzip_io, mode='wb', compresslevel=1) as gz:
                shutil.copyfileobj(ts_io, gz)

            threads = [*threads , \
                Thread(target=S3Upload,args=(gzip_io, tag_path+'.gzip', mtime) )]

        if self.sharedData.save_local:
            threads = [*threads , \
                Thread(target=SharedDataTimeSeries.write_file, args=(ts_io, tag_path, mtime) )]
                            
        for i in range(len(threads)):
            threads[i].start()

        for i in range(len(threads)):
            threads[i].join()

    def create_timeseries_io(df):
        df = df.dropna(how='all',axis=0)
        r, c = df.shape
        idx = (df.index.astype(np.int64))
        idx_b = idx.values.tobytes()
        cols = df.columns.values
        colscsv = ','.join(cols)
        colscsv_b = str.encode(colscsv,encoding='UTF-8',errors='ignore')
        nbidx = len(idx_b)
        nbcols = len(colscsv_b)
        data = np.ascontiguousarray(df.values.astype(np.float64))
        header = np.array([r,c,nbidx,nbcols,r*c*8]).astype(np.int64)
        #calculate hash
        m = hashlib.md5(idx_b)
        m.update(colscsv_b)
        m.update(data)
        md5hash_b = m.digest()
        # allocate memory
        io_obj = io.BytesIO()
        io_obj.write(header)
        io_obj.write(idx_b)
        io_obj.write(colscsv_b)
        io_obj.write(data)
        io_obj.write(md5hash_b)
        return io_obj

    def write_file(io_obj,path,mtime):
        with open(path, 'wb') as f:
            f.write(io_obj.getbuffer())
            f.flush()
        os.utime(path, (mtime, mtime))

    # MESSAGES
    def broadcast(self,idx,col):
        SharedDataRealTime.broadcast(
            self.sharedData,
            self.feeder,
            self.period,
            self.tag,
            idx,col)
    
    # get / set
    def get_loc_symbol(self, symbol):
        if symbol in self.symbolidx.keys():
            return self.symbolidx[symbol]
        else:
            return np.nan

    def get_loc_timestamp(self, ts):
        istartdate = self.startDate.timestamp() #seconds
        if not np.isscalar(ts):
            tidx = self.get_loc_timestamp_Jit(ts, istartdate, \
                self.periodSeconds, self.ctimeidx)            
            return tidx
        else:
            tids = np.int64(ts) #seconds
            tids = np.int64(tids - istartdate)
            tids = np.int64(tids/self.periodSeconds)
            if tids<self.ctimeidx.shape[0]:
                tidx = self.ctimeidx[tids]
                return tidx
            else:
                return np.nan
    
    @staticmethod
    @jit(nopython=True, nogil=True, cache=True)
    def get_loc_timestamp_Jit(ts, istartdate, periodSeconds, ctimeidx):
        tidx = np.empty(ts.shape, dtype=np.float64)
        len_ctimeidx = len(ctimeidx)
        for i in range(len(tidx)):
            tid = np.int64(ts[i])
            tid = np.int64(tid-istartdate)
            tid = np.int64(tid/periodSeconds)
            if tid < len_ctimeidx:
                tidx[i] = ctimeidx[tid]
            else:
                tidx[i] = np.nan
        return tidx
    
    @staticmethod
    @jit(nopython=True, nogil=True, cache=True)
    def setValuesSymbolJit(values,tidx,sidx,arr):
        if not np.isnan(sidx):
            s = np.int64(sidx)
            i = 0
            for t in tidx:
                if not np.isnan(t):
                    values[np.int64(t),s] = arr[i]
                i=i+1

    @staticmethod
    @jit(nopython=True, nogil=True, cache=True)
    def setValuesJit(values,tidx,sidx,arr):
        i = 0
        for t in tidx:
            if not np.isnan(t):
                j = 0
                for s in sidx:
                    if not np.isnan(s):
                        values[np.int64(t),np.int64(s)] = arr[i,j]
                    j=j+1
            i=i+1

    # C R U D     
    def malloc(self, value=None):
        tini=time.time()
        
        #Create write ndarray
        path, shm_name = self.get_path()
        
        if os.environ['LOG_LEVEL']=='DEBUG':
            Logger.log.debug('malloc %s ...%.2f%% ' % (shm_name,0.0))

        try: # try create memory file
            r = len(self.index)
            c = len(self.columns)
                        
            idx_b = self.index.astype(np.int64).values.tobytes()
            colscsv_b = str.encode(','.join(self.columns.values),\
                encoding='UTF-8',errors='ignore')
            nb_idx = len(idx_b)
            nb_cols = len(colscsv_b)
            nb_data = int(r*c*8)
            header_b = np.array([r,c,nb_idx,nb_cols,nb_data]).astype(np.int64).tobytes()
            nb_header = len(header_b)
            
            nb_buf = nb_header+nb_idx+nb_cols+nb_data
            nb_offset = nb_header+nb_idx+nb_cols

            [self.shm, ismalloc] = self.sharedData.malloc(shm_name,create=True,size=nb_buf)
            
            i=0
            self.shm.buf[i:nb_header] = header_b
            i = i + nb_header
            self.shm.buf[i:i+nb_idx] = idx_b
            i = i + nb_idx
            self.shm.buf[i:i+nb_cols] = colscsv_b

            self.shmarr = np.ndarray((r,c),\
                dtype=np.float64, buffer=self.shm.buf, offset=nb_offset)
            
            if not value is None:
                self.shmarr[:] = value.values.copy()
            else:
                self.shmarr[:] = np.nan
            
            self.data = pd.DataFrame(self.shmarr,\
                        index=self.index,\
                        columns=self.columns,\
                        copy=False)
            
            if not value is None:
                value = self.data

            if os.environ['LOG_LEVEL']=='DEBUG':
                Logger.log.debug('malloc create %s ...%.2f%% %.2f sec! ' % \
                    (shm_name,100,time.time()-tini))            
            self.create_map = 'create'
            return True
        except Exception as e:
            pass
                        
        # map memory file
        [self.shm, ismalloc] = self.sharedData.malloc(shm_name)
        
        i=0
        nb_header=40
        header = np.frombuffer(self.shm.buf[i:nb_header],dtype=np.int64)
        i = i + nb_header
        nb_idx = header[2]
        idx_b = bytes(self.shm.buf[i:i+nb_idx])
        self.index = pd.to_datetime(np.frombuffer(idx_b,dtype=np.int64))
        i = i + nb_idx
        nb_cols = header[3]
        cols_b = bytes(self.shm.buf[i:i+nb_cols])
        self.columns = cols_b.decode(encoding='UTF-8',errors='ignore').split(',')

        r = header[0]
        c = header[1]        
        nb_data = header[4]
        nb_offset = nb_header+nb_idx+nb_cols                
        
        self.shmarr = np.ndarray((r,c), dtype=np.float64,\
             buffer=self.shm.buf, offset=nb_offset)

        self.data = pd.DataFrame(self.shmarr,\
                    index=self.index,\
                    columns=self.columns,\
                    copy=False)
        
        if not value is None:
            iidx = value.index.intersection(self.data.index)
            icol = value.columns.intersection(self.data.columns)
            self.data.loc[iidx, icol] = value.loc[iidx, icol]

        if os.environ['LOG_LEVEL']=='DEBUG':
            Logger.log.debug('malloc map %s/%s/%s ...%.2f%% %.2f sec! ' % \
                (self.feeder,self.period,self.tag,100,time.time()-tini)) 
        self.create_map = 'map'
        return False
    
    def free(self):
        path, shm_name = self.get_path()            
        self.sharedData.free(shm_name)