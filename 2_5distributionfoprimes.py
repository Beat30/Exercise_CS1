#Ex. 2.5
#Plot prime numbers

import numpy as np
import matplotlib.pyplot as plt
import pylab
import math

primes=[]
notprimes=[]
y=[]
k=2

for i in range(3,4000,2):
    iprimes=[x*i for x in primes]
    notprimes+=iprimes
    notprimes+=[i*i]
    if i not in notprimes:
        primes+=[i]
        y+=[k*math.log(i)]
        k+=1

plt.plot(primes,y, linestyle=':')
plt.xlabel('$P_{k}$')
plt.ylabel('$k*log(P_k)$')
plt.title('Distribution of primes')
pylab.show()
