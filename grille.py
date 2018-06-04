import random
import string
v = input("Enter a plain text:")
grile = [[0 for x in range(len(v))] for y in range(len(v))]
f = list(range(0,len(v)))
o = list(range(0,len(v)))
d = random.sample(f,len(v))
c = random.sample(o,len(v))
for i in range(len(v)):
    grile[d[i]][c[i]] = v[i]
    
for x in range(len(v)):
    for y in range(len(v)):
        if grile[x][y] == 0:
            grile[x][y] = random.choice(string.ascii_lowercase)
key = ""
for i in range(len(v)):
    for y in range(len(v)):
        key = key + grile[i][y]
print("Enciphered key: ",key)
#####################decipher
print("Deciphered: a",end='')
for i in range(len(d)):
    print(grile[d[i]][c[i]],end='')

