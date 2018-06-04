import random
import math
##a = input('Enter a plain text:')
##s=0
##for i in a:
##    s=s+ord(i)
################
#text = input("Enter text: ")
primes = []
two_primes =[]
def main():
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
two_primes = sorted(random.sample(primes,2))
print(two_primes)
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
    #Phi is the totient of n
    phi = (p-1) * (q-1)
    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    #Return public and private keypair
    
    
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))
qe, qq = (generate_keypair(two_primes[0], two_primes[1]))
print('public:', qe,'private:', qq)
