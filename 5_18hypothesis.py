

import numpy as np
from numpy import pi, arange, concatenate
from pylab import subplot, plot, show
import random as rd

N=60
M=500
random=[]
random+=[-1]*N
random+=[1]*N
ss=[]
for j in range(M):
    rd.shuffle(random)
    s=[]
    for i in range(0,2*N):
        if i==0:
            s+=[random[i]]
        else:
            s+=[s[i-1]+random[i]]
            
    s=np.array(s)
    smax=max(s)
    smin=min(s)
    ss+=[max(abs(s))]
    
ss=np.array(ss)/N


pks=0
d=24.
m=36.
nu=np.sqrt(d*m/(d+m))
mu=nu+0.12+0.11/nu

for k in range(1000):
    pks+=2*(-1)**k*np.exp(-2*((k+1)*mu*ss)**2)


plot(ss,1-pks,'b.')
show()
