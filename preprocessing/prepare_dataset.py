#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import os
import requests
import rasterio
import numpy as np
import pyproj
from rasterio import windows
import matplotlib.pyplot as plt


def openraster(filename):
    if  os.path.exists(filename):
        return rasterio.open(filename)
    
    


def findlatlon(reader, col, row):
    
    x, y = reader.xy(col, row)
    p = pyproj.Proj(reader.crs)
    lon, lat = p(x, y, inverse=True)
    return lon, lat
    


filedir = '/Volumes/Seagate Backup Plus Drive/wildfiredataset/'
dataset_df = pd.DataFrame(columns=['filename', 'latitude','longitude', 'width','height'])
i=1
for item in os.listdir(os.path.join(filedir,'ndvi')):
    #print(item)
    reader = openraster(os.path.join(filedir,'ndvi', item))
    print("reader:{}".format(i))
    i+=1
    for ji, window in reader.block_windows(1):
        
        subset = reader.read(1, window=windows.Window(window.col_off, window.row_off, 
                                                         window.width , window.height))
        
        filename, extension = os.path.splitext(item)
        filename = filename+"_window_{}_{}".format(ji[0],ji[1])
        filename = filename+extension
        #plt.imshow(subset)
        print(filename)
        new_dataset = rasterio.open(
         os.path.join(filedir, 'ndviblocks',filename),
         'w',
         driver='GTiff',
         height=window.height,
         width=window.width,
         count=1,
         dtype=subset.dtype,
         crs='+proj=latlong',
         transform=reader.window_transform(window),
         )
        new_dataset.write(subset, 1)
        
        lon_min, lat_min = findlatlon(reader, window.col_off, window.row_off)
        
        
        data=[[filename, lat_min, lon_min, window.width, window.height]]
        df_temp = pd.DataFrame(data=data,columns=['filename', 'latitude','longitude', 'width','height'])
        dataset_df = dataset_df.append(df_temp) 



new_dataset.close()


dataset_df.to_csv(filedir+"dataset.csv")






