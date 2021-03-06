
#Working with matplotlib 

#for the line plot

#import matplotlib.pyplot as plt
#import numpy as np
#
#a = np.linspace(10,70,70)
#
#b = np.exp(-a)
#
#plt.plot(a,b)
#
#plt.show()


#This is for 3-D plot  

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-1,5, 0.25)
Y = np.arange(1, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
plt.show()

