# Project Euler Problem 58
# by Connor Halleck-Dube

import time
t0 = time.clock()

from primesmodule import isPrimeMR

## Solution 1: Iterative, only outer loop at a time

# Number of primes on the outer diagonal of spiral length side
def spiralPrimes(side):
    b = side**2
    shift = side-1
    return sum([isPrimeMR(b-i*shift) for i in range(1,4)])

total = 5
side = 3
diagprimes = 3
while (diagprimes/total > 0.1):
    total += 4
    side += 2
    diagprimes += spiralPrimes(side)
print(side)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
