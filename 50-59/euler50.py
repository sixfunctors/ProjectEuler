# Project Euler Problem 50
# by Connor Halleck-Dube

import time
t0 = time.clock()

from primesmodule import isPrimeMR

## Solution 1: Pre-generate primes, check lengths downward from an upper-bound

UPPERBOUND = 700

# generate primes under 1000000
witnesses = [2, 3, 5]
primes = [2]
for n in range(3, 1000000, 2):
    if isPrimeMR(n):
        primes.append(n)
primeset = set(primes)

# Prints the sum of l successive primes beginning with the ith.
def sumByIndex(i, l):
    
    return sum(primes[i:i+l])

found = False # Tracks whether we find a sum of given length
l = UPPERBOUND # The solution is probably no longer than 700
while not found:
    found = False
    for i in range(len(primes)-l):
        s = sumByIndex(i, l)
        if s in primeset:
            print(s)
            found = True
            break
    l -= 1


## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
