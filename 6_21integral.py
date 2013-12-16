# Ex. 6.21
# Integrate e**(-x**2)


import math
import numpy as np
from numpy import pi, arange, matrix
from scipy import fft, linalg
from pylab import subplot, plot, show
import random as r
import matplotlib as mplib
from scipy.linalg import solve
########################################################################
def gauss(x):
    #x=(a,b)
    x=np.array(x)
    f=math.e**(-x**2)
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
    m=len(f)/(2*10) #b=10
    t=len(f)/2
    h=((a+yb)//2)*m+t #mid of intervall
    print(h)
    intf=c4*(f[(h-4)]+f[(h+4)])+c2*(f[(h-2)]+f[(h+2)])+c0*f[(h)]
    print(intf)
    return intf

def fivepoint(f,a): #a,b limits, (b-a)%10==0!!!
    B=len(f)//10#B=no of intervalls
    aa=[]
    bb=[]
    integral=0
    for i in range(B):#new limits
        bb+=[a+(1+i)*2]
        aa+=[a+i*2]
        integral+=iint(f,aa[i],bb[i])
    integral=float(integral)/5
    return integral
########################################################################

b=10
a=-b
n=100
x=np.linspace(a,b,n)
f=gauss(x)
print('integral=',fivepoint(f,a))
print('squareroot of pi=',math.sqrt(pi))
plot(x,f)
show()
