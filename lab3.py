plaintext=input("Enter a plain word: ")
key_word=input("Enter a key word: ")
plaintext_int=[ord(i) for i in plaintext]
key_int=[ord(i) for i in key_word]
c=[]
r=[]
for i in range(len(plaintext)):
    value = (plaintext_int[i] + key_int[i % len(key_word)]) % 97
    c.append(value+97)
for i in c:
    if i>122:
        i=i-26
        r.append(i)
    else:
        r.append(i)
for x in r:
    print(chr(x),end='')
