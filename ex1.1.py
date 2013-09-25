#Ex. 1.1

#Deadline for changing to 64-bit integers:
import time
print('Deadline for changing to 64-bit integers is',time.gmtime(pow(2,32)-1))


#find the number of bits of a floating number
eps=.5
n=0

while 1+eps!=1:
    eps=eps/2
    n+=1


print('No. of bits for mantissa=', n)

#exp
e=1
while 2**(-2**e) != 0:
    e+=1

print('No. of bits for exponent=', e)

print('No. of bits for sign=', 64-e-n)
