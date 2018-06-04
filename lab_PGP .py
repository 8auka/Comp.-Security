import math
import random
import zlib

text = raw_input("Enter text: ")
primes = []
two_primes =[]
hash_count = 0

#HASH
for i in text:
    hash_count += ord(i)

#PRIME NUMBERS
def PrimeNumber():
    count = 3
    while count<70:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        if isprime:
            primes.append(count)
        count += 1
PrimeNumber() #call function
two_primes = sorted(random.sample(primes,2))

##RSA
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi
def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))
public, private = (generate_keypair(two_primes[0], two_primes[1]))
print 'Public key: ', public,'Private key: ', private


##Encrypt Ceaser Cipher
encryptedWithCipher = ""
for i in text:
    encryptedWithCipher += chr(ord(i) + 1)

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher
encrypted_message = encrypt(private,encryptedWithCipher)
rsa_encr = ''.join(map(lambda x: str(x), encrypted_message))
print 'Encrypted with RSA version: ',rsa_encr


def comp_test(s):
    c = str(s).encode()
    return zlib.compress(c)
##Compress
comp = comp_test(encrypted_message)
print ('Compress version: ', comp)




##DECRYPTION
##Decompress
def decomp_test(s):
    c = zlib.decompress(s)
    return c.encode()

decomp = decomp_test(comp)
print 'Decompress version: ',decomp

##l = []
##for i in range(0, len(encrypted_message)):
##    if i == 0:
##        l.append(decomp.split(', ')[i][1:])
##    elif i == len(encrypted_message)-1:
##        l.append((decomp.split(', ')[i][:-1]))
##    else:
##         l.append(decomp.split(', ')[i])
##print(l,type(l))

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    print()
    return ''.join(plain)
decryptWithCipher = decrypt(public,encrypted_message)

##Decrypt with ceaser cipher
l = ""
for i in decryptWithCipher:
    l += chr(ord(i)-1)

print 'Decrypted text: ',l 

hash_count2 = 0
for i in l:
    hash_count2 += ord(i)
if hash_count == hash_count2:
    print('Your message ok')
else:
    print('Your message was hacked')



