# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:57:56 2020

Mocks the behaviour of a time series database with index on time, resulting
in access times roughly linear to the number of time steps read.

@author: Pascal Dubucq
"""

import time

import pandas as pd
import numpy as np

#%%

random_data = lambda r,c: pd.DataFrame(data=np.random.uniform(r * -.099, r * .1, (r, c)), 
                    columns=[f"var{i}" for i in range(c)], 
                    index=pd.date_range(pd.Timestamp("now"), freq="H", 
                                        periods=r, name="DATETIME")).cumsum()

class DataBaseClient():
    
    def __init__(self, nrows, ncols, sleep):
        self._nrows = nrows
        self._ncols = ncols
        self._sleep = sleep
        
    def read(self, id, start=None, end=None):
        id_data = random_data(self._nrows, self._ncols)
        return_data = id_data.loc[start:end]
        time.sleep(self._sleep * return_data.shape[0]/id_data.shape[0])
        return return_data
    
    def read_index(self, id, idx_start=None, idx_end=None):
        id_data = random_data(self._nrows, self._ncols)
        return_data = id_data.iloc[idx_start:idx_end]
        time.sleep(self._sleep * return_data.shape[0]/id_data .shape[0])
        return return_data    
    
    def read_from(self, id, start, nhours):
        return self.read(id, start, start + pd.DateOffset(hours=nhours))
    
    def ids(self):
        time.sleep(self._sleep * .1)
        return list(range(600))