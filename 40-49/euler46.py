# Project Euler Problem 46
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import sqrt

## Solution 1: Procedurally generate primes, iterate through odd composites

# Miller-Rabin Primality
witnesses = [2, 3, 5, 7, 11] # accurate for n < 2 152 302 898 747
def isPrimeMR(n):
    if (n == 2):
        return True
    elif (n <= 1) or (n%2 == 0):
        return False
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
                break # this a is not a witness
        if poswitness: # a is a witness for n
            return False
    return True

# Checks whether the composite is expressible as the sum of a prime and double a square
primes = set([2])
def isExpressible(n):
    for p in primes:
        diff = (n-p)/2
        if diff <= 0:
            continue
        elif sqrt(diff).is_integer():
            return True
        else:
            continue
    return False

# iterate through odd composites
n = 3
while True:
    if isPrimeMR(n):
        primes.add(n)
        n += 2
        continue
    elif isExpressible(n):
        n += 2
        continue
    else:
        break
print(n)
    

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
