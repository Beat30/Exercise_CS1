# Ex. 5.15 Plot the first 512 numbers, using base 2 for x and base 3 for y

from pylab import subplot, plot, show


N=512


def convert(N,b): #Generate the first N numbers of a Halton sequence unsing base b
    halton=[]
    for i in range(1,N):
        n=i
        k=[0]
        while (n>0):
            a=int(n%b)
            k.append(a)
            n=(n-a)/b
        
        e=0
        z=0
        for j in k:
            z+=j*b**e
            e-=1
        halton+=[z]
        
    return halton


halton2= convert(N,2)
halton3= convert(N,3)
plot(halton2,halton3,'b.')
show()
