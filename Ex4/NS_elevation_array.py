import numpy as np
from osgeo import gdal
from matplotlib import pyplot as plt
from matplotlib import cm

"""
How to fully load a raster image into a NumPy array:
http://gis.stackexchange.com/questions/32995/how-to-fully-load-a-raster-into-a-numpy-array
"""

dataset = gdal.Open("NS_DEM_merged_high_compression.tif")

data = np.array(dataset.GetRasterBand(1).ReadAsArray())

data.shape

"""
Get UTM corner points from plotting
"""

data.ptp()

"""
Make an awesome image
"""
step = 1 #change this if you want to decimate the data

plt.figure(figsize = [20,8], facecolor='white' )
plt.imshow(data[:4500:step,1700:10000:step], cmap = cm.gist_earth_r, vmin = 0, vmax=525)
plt.colorbar(shrink=0.75)
plt.show()

"""A to A'"""
plt.figure(figsize = [20,3])
plt.plot(data[:,3000])
plt.show()


"""B to B'"""
#plt.figure(figsize = [20,3])
#plt.plot(data[2500,:])
#plt.show()
