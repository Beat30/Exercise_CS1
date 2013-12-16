# Ex. 2.7
# RSA Encryption

'''
N public key

Bob has announced his public key as N = 1024384027, c = 910510237. Alice
encrypts her plaintext a using the public key and send the cyphertext b = 100156265
by an open channel. Bob uses his private key to recover a and hence the word.
Eve sees b = 100156265 on the open channel.
She writes a program to solve pow(b,r,N)==1 for r.
With r in hand, she recovers a and finally the secret word.
What was the word Alice wanted to send?
'''

n=1
import math

def word(n): #to extract the integer n
    str=" "
    while n>0:
        c= chr(n%32+96)
        if c < "a" or c > "z":
            c=" "
        str+=c
        n//=32
    return str


N=1024384027 #Public key
c=910510237 #public key
b=100156265 #cyphertext sent by Alice throug an open channel to Bob

br=b
r=1

#### find r with pow(a,r,N)==1
while br!=1:
    br=(br*b)%N
    r+=1
print('r=', r)


d=1
while ((c*d)%r != 1):
    d+=1

a=pow(b,d,N)

print('The message is: ', word(a))
