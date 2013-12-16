#random walk and the central limit theorem

import numpy as np
from pylab import subplot, plot, show
import random as rd
import matplotlib

s=[]
N=100

#Generate 10000 numbers which are the sum of N times -1 or 1
for j in range(10000): 
    d=0
    for i in range(N): 
        d+=rd.randrange(-1,2,2) 

    s+=[d]

s=np.array(s)
s_abs=np.abs(s)

subplot(2,1,1)
matplotlib.pyplot.hist(s, bins=N/5, range=None, histtype='bar')

subplot(2,1,2)
matplotlib.pyplot.hist(s_abs, bins=N/5, range=None, histtype='bar')
show()
