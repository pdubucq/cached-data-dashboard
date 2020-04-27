# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:13:04 2020

Test the mock implementation of a database

@author: Pascal Dubucq
"""

import pytest

import pandas as pd

from database_mock import DataBaseClient

SAMPLE_DATA_ROWS = 10
SAMPLE_DATA_COLS = 2
SAMPLE_DATA_SLEEP = 0

# tests/test_console.py
@pytest.fixture
def dbclient():
    return DataBaseClient(SAMPLE_DATA_ROWS, 
                          SAMPLE_DATA_COLS, 
                          SAMPLE_DATA_SLEEP)

def test_read_full(dbclient):
    assert isinstance(dbclient.read(1), pd.DataFrame)
    
def test_read_empty_time_range(dbclient):
    assert dbclient.read(1, None, "1900").empty
    
def test_read_index(dbclient):
    assert dbclient.read_index(1, 0, 5).shape == (5, SAMPLE_DATA_COLS)
    
def test_read_from(dbclient):
    now = pd.Timestamp('now')
    ref = pd.Timestamp(now.year, now.month, now.day, now.hour)
    assert dbclient.read_from(1, ref, 2).shape \
                == (2, SAMPLE_DATA_COLS)
                
def test_ids_list(dbclient):
    assert isinstance(dbclient.ids(), list)
    
def test_ids_not_empty(dbclient):
    assert len(dbclient.ids()) > 0