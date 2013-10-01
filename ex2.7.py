# Ex. 2.7
# RSA Encryption
n=1

def word(n):
    str=" "
    while n>0:
        c= chr(n%32+96)
        if c < "a" or c > "z":
            c=" "
        str+=c
        n//=32
    return str


N=1024384027
c=910510237
b=100156265

br=b
r=1

while br!=1:
    br=(br*b)%N
    r+=1
print(r)


while ((a**r)%N != 1):
    a+=1

print('The message is: ', word(a))
