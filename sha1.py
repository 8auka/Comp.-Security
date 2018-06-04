import hashlib
while True:
    i = input("Enter a word:")
    v=i.encode()
    s = hashlib.sha1(v)
    print("SHA-1 of",str(i),"is:",s.hexdigest())
