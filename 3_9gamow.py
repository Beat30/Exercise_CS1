from itertools import permutations


dict={}
a=1
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            
            dict[a]=[i,j,k,(j+2)%4]
            a+=1

###delete double solutions
for i in range(1,64):
    for j in range(i+1,65):
        try:
            if (dict[i][0]==dict[j][0]) and (dict[i][1]==dict[j][3]) and (dict[i][2]==dict[j][2]) and (dict[i][3]==dict[j][1]):
                del dict[j]
            if (dict[i][0]==dict[j][2]) and (dict[i][1]==dict[j][3]) and (dict[i][2]==dict[j][0]) and (dict[i][3]==dict[j][1]):
                del dict[j]
            if (dict[i][0]==dict[j][2]) and (dict[i][1]==dict[j][1]) and (dict[i][2]==dict[j][0]) and (dict[i][3]==dict[j][3]):
                del dict[j]
            
        except KeyError:
            pass

###convert number to letter
num_to_letter = { 0:'A', 1:'C', 2:'T', 3:'G'}
try:
    for i in dict:
        for j in range(0,4):
            dict[i][j]=num_to_letter[dict[i][j]]
except KeyError:
    pass

###Print solutions        
print('There are the following', len(dict), 'different Gamow diamonds:')
for item in dict:
    print(dict[item])
