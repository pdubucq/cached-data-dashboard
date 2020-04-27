# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:37:39 2020

@author: acf10
"""

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.plotting import figure, curdoc, show
from bokeh.models import ColumnDataSource

import pandas as pd
from dbmock import DataBaseClient

# create a plot and style its properties
p = figure(x_axis_type='datetime')

dbclient = DataBaseClient(20, 10, 1)

df = dbclient._data

df['DATETIME'] = pd.to_datetime(df.index, format='%m/%d/%Y')

plotdata = ColumnDataSource(df)

# create a callback that will add a number in a random location
r = p.line(x="DATETIME", y="var1", source=plotdata)

show(p)