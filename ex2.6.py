#Ex. 2.6
#Find Carmichael numbers between 1 and N

import numpy as np
import matplotlib.pyplot as plt
import pylab
import math
import fractions as fr

N=7000
primes=[]
notprimes=[]
y=[]
k=1

for i in range(2,N):
    iprimes=[x*i for x in primes]
    notprimes+=iprimes
    notprimes+=[i*i]
    if i not in notprimes:
        primes+=[i]
        y+=[k*math.log(i)]
        k+=1

nprime=[]
for x in range(2,N):
    if x not in primes:
        nprime += [x]

##
for q in nprime:
    c=1
    a=2
    while (a < q) and (c!=0):
        if fr.gcd(a,q)==1:
            if pow(a,q-1,q)!=1:
                c=0
        a+=1
    if (c!=0) and (a<=q):
        print(q)




