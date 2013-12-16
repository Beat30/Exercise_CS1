#9.35 vampires
#Beat Lauber

from math import cos, sin, pi
import numpy as np
import scipy
import matplotlib
import matplotlib.pyplot as plt

def vampire(f): #f= list or array
    global dx
    pf=list(f)
    del pf[0]
    pf+=[0.]
    
    nf=list(f)
    del nf[-1]
    nf=[0.]+nf
    f=np.array(f)
    nf=np.array(nf)
    pf=np.array(pf)
    df=f*(1-f)+dx**(-2)*(pf+nf-2*f)
    return df #return array


def leapfrog(vampire,f0,tmax,dt): #f0=liste
    ti=[0]
    fi=[f0]
    mmax=int((tmax)/dt +1)
    for m in range(1,mmax,1):
        tn=ti[m-1]
        fn=fi[m-1]
        fn=np.array(fn)
        df1=fn+1/2*dt*vampire(fn)
        df2=fn+dt*vampire(df1)
        df2=list(df2)       
        ti+=[tn+dt]
        fi=fi+[df2]
    return [ti,fi]

if __name__ == '__main__' :
    
    pop=0.00001
    xmax=10
    xmin=-xmax
    dx=1
    tmax=10
    dt=0.1
    xx=np.arange(xmin,xmax+1,dx)
    
    ffunction=list(np.zeros(xmax/dx))+[pop]+list(np.zeros(xmax/dx))

        
    [t, endfunction]=leapfrog(vampire,ffunction,tmax,dt)
    t=np.array(t)
    endfunction=np.array(endfunction)
    totalendfunctiontime=endfunction[:,1]
    totalendfunctionspace=endfunction[50,:]
    print ('endfunction is', endfunction)
    print ('totalendftime is', totalendfunctiontime, len(totalendfunctiontime))
    print ('totalendfspace is', totalendfunctionspace, len(totalendfunctionspace))
    print ('xx is', xx , len(xx))
    print ('time is', t , len(t))
    
    
    plt.subplot(211)
    plt.plot(t,totalendfunctiontime)
    plt.subplot(212)
    plt.plot(xx,totalendfunctionspace)
    plt.show()    
