#Ex. 1.4
#calculate pi

def arctan(A):
    i=0
    x=0.0
    y=1.0

    def fkt(A,i):
        x=A**(2*i+1)/(2*i+1)*(-1)**i
        return x
    while x!=y:
        y=x
        x+=fkt(A,i)
        i+=1

    return x

print('pi= ', 16*arctan(1/5)-4*arctan(1/239))
