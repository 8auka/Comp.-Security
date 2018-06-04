import collections
s = input("Type a word: ")
v=(collections.Counter(s).most_common(1)[0])
n=v[0]
x= ord(n)-ord("e")
for i in range(len(s)):
    if (ord(s[i])-x)>122:
        print(chr(ord(s[i])-x-26),end='')
    else:
        print(chr(ord(s[i])-x),end='')
