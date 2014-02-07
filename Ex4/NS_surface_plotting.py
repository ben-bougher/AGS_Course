"""
3D plotting
"""

"""
Make a surface plot (Matplotlib)
http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#Axes3D.plot_surface(X, Y, Z, *args, **kwargs)
"""

"Make a surface plot (Mayavi)"""
import numpy as np
from osgeo import gdal
dataset = gdal.Open("NS_DEM_merged_high_compression.tif")

data = np.array(dataset.GetRasterBand(1).ReadAsArray())

from mayavi import mlab
mdata = data[::25, ::25]
aux = np.transpose(mdata)
mdata = np.fliplr(aux)

mlab.figure(size=(400, 320), bgcolor=(0.16, 0.28, 0.46))
mlab.surf(mdata, colormap='gist_earth', warp_scale = 0.05,
            vmin=mdata.min(), vmax=mdata.max() )
# The data takes a lot of memory, and the surf command has created a
# copy. We free the inital memory.
del data

# A view of Nova Scotia
mlab.view(-5.9, 83, 570, [5.3, 20, 238])
mlab.show()