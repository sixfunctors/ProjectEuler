# Project Euler Problem 47
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import sqrt
from primesmodule import isPrimeMR

## Solution 1: Generate primes alongside test

# Number of prime factors of a number (distinct ones)
def pfactors(num):
    count = 0
    n = num
    for p in primes:
        if n%p == 0:
            count += 1
            n //= p
    return count
    
# Tests the x consecutive integers property, beginning with n
def consecTest(n, x):
    for i in range(x):
        if (pfactors(n+i) < x):
            return False
    return True

# iterate until you find one
n = 1
primes = set()
while True:
    if isPrimeMR(n):
        primes.add(n)
    
    if consecTest(n, 4):
        break
    n += 1
print(n)


## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
