# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:17:12 2020

@author: acf10
"""

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.plotting import figure, curdoc, show
from bokeh.models import ColumnDataSource, Slider, Select
from bokeh.palettes import RdYlBu3


import pandas as pd
from database_mock import DataBaseClient

# create a plot and style its properties
plot_time = figure(x_axis_type='datetime')

N_steps = 8760
dbclient = DataBaseClient(N_steps, 10, 60)

#df['DATETIME'] = pd.to_datetime(df.index, format='%m/%d/%Y')

# Create Column Data Source that will be used by the plot
plotdata = ColumnDataSource(data=dict(DATETIME=[], var0=[]))

r = plot_time.line(x="DATETIME", y="var0", source=plotdata)

# control elements
slider_start = Slider(title="Start index", value=0, start=0, end=N_steps, 
                 step=N_steps // 100)

slider_end = Slider(title="End index", value=168, start=0, end=N_steps, 
                 step=N_steps // 100)

button_update = Button(label="Update Plot")

button_cache = Button(label="Save id data in cache (parquet file)")

selectbox_id = Select(title="ID", 
                      value="1", 
                      options=[str(i) for i in dbclient.ids()])


def selection():
    "returns the pandas dataframe matching the selection criteria"
    idx_min = slider_start.value
    idx_max = slider_end.value
    id = int(selectbox_id.value)
    df = dbclient.read_index(id, idx_min, idx_max)
    return df.reset_index()[['DATETIME', 'var0']]
    
def update():
    plotdata.data = selection()
    
def fill_cache():
    dbclient.fill_cache(int(selectbox_id.value))
    
# control actions
button_update.on_click(update)
button_cache.on_click(fill_cache)

# initial creation of data
update()

# put the button and plot in a layout and add to the document
curdoc().add_root(column(slider_start, slider_end, button_update, plot_time))