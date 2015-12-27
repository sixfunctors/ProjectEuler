# Project Euler Problem 7
# by Connor Halleck-Dube

from random import randrange


import time
t0 = time.clock()

## Solution 1: Naive Solution - Unreasonably long
"""
def isPrime1(n):
    for i in range(2, n):
        if (n%i == 0):
            return False
    return True

p = 0
i = 1
while (p<10001):
    i += 1
    
    if isPrime1(i):
        p += 1

print(i)
"""
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")

## Solution 2: Probabilistic primality test with reliable witness set
# sufficient witnesses for all n < 341 550 071 728 321
witnesses = [2, 3, 5, 7, 11, 13, 17]

# Miller-Rabin
def isPrime2(n):
    s = 0
    d = n - 1
    while (d%2 == 0):
        d //= 2
        s += 1
    
    for a in witnesses:
        if (a >= n):
            continue
        
        if (pow(a, d, n) == 1):
            continue # this a is not a witness
        
        poswitness = True
        for r in range(0, s):
            if (pow(a, d*pow(2, r), n) == n-1):
                poswitness = False
                break #this a is not a witness
        
        if poswitness: # a is a witness for n
            return False
    
    return True
        
        
p = 0
i = 1
while (p<10001):
    i += 1
    
    if isPrime2(i):
        p += 1

print(i)
## End Solution 2

t2 = time.clock()
print("Solution 2 took:", round(t2-t1, 4), "seconds.")
    