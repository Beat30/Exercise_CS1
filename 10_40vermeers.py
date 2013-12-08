#Vermeers Window
#Beat Lauber


from matplotlib.image import imread
from pylab import imshow, contour, show, array
from time import time
from numpy import *
from scipy.optimize import leastsq
import numpy as np




def func(p, grid, window):
    a,b,c,d=p[0],p[1],p[2],p[3]
    x=grid[0]
    y=grid[1]
    X=window[0]
    Y=window[1]
    err=(a*d-X*(x+c))**2+((x+b)*d-Y*(x+c))**2
    return err


gridx=array([-1,0,1,-1,0,1,-1,0,1])
gridy=array([1,1,1,0,0,0,-1,-1,-1])
grid=np.array([gridx,gridy])

windowx = array([59,77,92,59,77,93,60,78,93])
windowy = array([216,226,236,274,282,287,332,336,338])
window=np.array([windowx,windowy])

x0=np.array([1.,1.,2.,1.])
xFit = leastsq(func, x0, args=(grid, window))
print(xFit)








