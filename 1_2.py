#Ex. 1.2
#calculate nth root of an integer A

y=0.0
x=1.0
n=2
A=float(input('Enter a number A>0: A= '))
x=A/2.0
def nroot(A,x,n):
    x=1/n*((n-1)*x+A/x**(n-1))
    return x

while x!=y:
    y=x
    x=nroot(A,x,n)
    
print( 'nth root of', A,' is ', x)
