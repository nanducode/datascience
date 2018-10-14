# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 03:13:14 2017

@author: anand
"""

import matplotlib.pyplot as plt
import matplotlib.cm
from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import numpy as np

#fig, ax = plt.subplots(figsize=(40,20))
def plotcountries(countrylist):
    m = Basemap(resolution='c', # c, l, i, h, f or None
               #projection='robin',
                projection = 'robin',
                lat_0=0, lon_0=0)
                #llcrnrlon=-6., llcrnrlat= 49.5, urcrnrlon=2., urcrnrlat=55.2)
    #m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
    #       llcrnrlon=-180,urcrnrlon=180,resolution='c')
    #m.drawmapboundary(fill_color='#46bcec')
    #m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
    geolocator = Nominatim()
    
    
    #m.drawcountries()
    #m.drawcoastlines()
    
    #plt.show()
    n_graticules = 18
    parallels = np.arange(-80., 90, n_graticules)
    meridians = np.arange(0., 360., n_graticules)
    lw = 1
    dashes = [5,7] # 5 dots, 7 spaces... repeat
    graticules_color = 'grey'
    fig1 = plt.figure(figsize=(16,20))
    fig1.patch.set_facecolor('#e6e8ec')
    ax = fig1.add_axes([0.1,0.1,0.8,0.8])
    
    m.drawmapboundary(color='white', 
                      linewidth=0.0, 
                      fill_color='white')
    m.drawparallels(parallels, 
                    linewidth=lw, 
                    dashes=dashes, 
                    color=graticules_color)
    m.drawmeridians(meridians, 
                    linewidth=lw, 
                    dashes=dashes, 
                    color=graticules_color)
    m.drawcoastlines(linewidth=0)
    m.fillcontinents('b', 
                     lake_color='white')
    m.drawcountries(linewidth=1, 
                    linestyle='solid', 
                    color='white', 
                    zorder=30)
    #m.readshapefile("borders/borders",name="countries",drawbounds=True)
   # country_names=[]
    #print(m.countries_info)
   ## for shape_dict in m.countries_info:
   #  country_names.append(shape_dict['NAME'])
    #print(country_names)
    #ax=plt.gca()
    x=[]
    y=[]
    for country in countrylist:
        print(country)
        try:
         locator = geolocator.geocode(country ,language = 'en')
         x1,y1=m(locator.longitude,locator.latitude)
         #print(locator.longitude,locator.latitude)
         #seg=m.countries[country_names.index(country)]
         #print(x,y)
         #poly = Polygon(seg, facecolor='red',edgecolor='red')
         
         #ax.add_patch(poly)
         x.append(x1)
         y.append(y1)
       
        
         
        except Exception as err:
            print(err)
    m.plot(x,y,'ro',markersize=5)
    title = plt.title('UN Goals', 
                      fontsize=20) 
    title.set_y(1.03) # Move the title a bit for niceness
    
#plotcountries(["India"])