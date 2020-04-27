# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:04:56 2020

@author: acf10
"""

from pathlib import Path

import pandas as pd

class CacheDataClient():
    
    def __init__(self, data_store_client, cache_dir):
        """ Initialize with a data store client providing the data
        and a directory where to store the cached data.

        data_store_client must implement 

        read(id, *args, **kwargs) -> pd.DataFrame

        if your data store does not, you should use an adapter class.

        """
            
        self.data_store_client = data_store_client
        
        self.cache_dir = cache_dir
        
        self.cache_files = {path.stem:path for path \
                            in Path(cache_dir).glob('*.pkl')}
            
    def read_cache(self, id, *args, **kwargs):
        """ Reads using the cache, if available, or else the data store """
        if self.cache_files.get(id):
            df = pd.read_pickle(self.cache_files[id])
            return df
        
        # else use data store client and create cache file
        return self.read_datastore(id, *args, **kwargs)
        
    
    def read_datastore(self, id, *args, **kwargs):
        """ Reads the data store and fills the cache"""
        df = self.data_store_client.read(id, *args, **kwargs)
        cache_file= Path(self.cache_dir) / f"{id}.pkl"
        df.to_pickle(cache_file, allow_truncated_timestamps=True)
        self.cache_files[id] = cache_file
        return df
    
    def clear_cache(self, id=None):
        """ Clear cache, either by id, or all in the directory """
        if id is not None:
            cache_file = self.cache_files.pop(id, None)
            if cache_file is not None and cache_file.exists():
                cache_file.unlink()
                
        else:
            # clear complete cache directory
            for cache_file in Path(self.cache_dir).glob('*.pkl'):
                cache_file.unlink()
                self.cache_files = {}
