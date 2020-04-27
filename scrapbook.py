# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:43:58 2020

@author: acf10
"""

from dbmock import DataBaseClient

SAMPLE_DATA_ROWS = 10
SAMPLE_DATA_COLS = 2
SAMPLE_DATA_SLEEP = 0


dbclient = DataBaseClient(SAMPLE_DATA_ROWS, 
                          SAMPLE_DATA_COLS, 
                          SAMPLE_DATA_SLEEP)

#%%