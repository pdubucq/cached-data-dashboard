# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:03:34 2020

@author: acf10
"""

import pytest

from dbmock import DataBaseClient
from cache_data_client import CacheDataClient

SAMPLE_DATA_ROWS = 10
SAMPLE_DATA_COLS = 2
SAMPLE_DATA_SLEEP = 0
CACHE_DIR = "cache"

@pytest.fixture
def dbclient():
    return DataBaseClient(SAMPLE_DATA_ROWS, 
                          SAMPLE_DATA_COLS, 
                          SAMPLE_DATA_SLEEP)

@pytest.fixture
def cacheclient(dbclient):
    return CacheDataClient(dbclient, CACHE_DIR)

def test_fixture(cacheclient):
    assert True