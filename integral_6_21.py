# Ex. 6.21
# Integrate e**(-x**2)


import math as m
import numpy as np
from numpy import pi, arange, matrix
from scipy import fft, linalg
from pylab import subplot, plot, show
import random as r
import matplotlib as mplib
from scipy.linalg import solve
########################################################################
def gauss(a,b):
    x=range(a,b)
    x=np.array(x)
    f=m.e**(-x**2)
    return f

def iint(f,a,yb):
#find coefficients
    M=matrix(((0.5,1,1),(0,4, 16),(0,16,256)))
    b=matrix( [[5],[25],[625]])
    xx=solve(M,b)
    c0=xx[0]
    c2=xx[1]
    c4=xx[2]
    #calculate integral
    h=(a+yb)//2 #mid of intervall
    intf=c4*(f[-4-h]+f[4-h])+c2*(f[-2-h]+f[2-h])+c0*f[-h]
    return intf

def fivepoint(f): #a,b limits, (b-a)%10==0!!!
    B=len(f)//2#B=no of intervalls
    bb=[]
    integral=0
    for i in range(B):#new limits
        bb+=[a+(1+i)*2]
        integral+=iint(f,a,bb[i])
    integral=float(integral)
    return integral
########################################################################

b=10
a=-b
f=gauss(a,b)
print('integral=',fivepoint(f))
print('squareroot of pi=',m.sqrt(pi))
plot(range(a,b),f)
show()
