# Project Euler Problem 60
# by Connor Halleck-Dube

import time

from primesmodule import isPrimeMR

f = open('workfile', 'w')

w = [2, 3, 5]
primes = []
for n in range(3, 20000000, 2):
    if isPrimeMR(n, w):
        primes.append(str(n))
print("Primes generated")
t0 = time.clock()

## Solution 1: Trusting that the value is below 10^7

def checkWith(s, prev):
    for p in prev:
        if ((not isPrimeMR(int(s+p), w)) or (not isPrimeMR(int(p+s), w))):
            return False
    return True

def anotherOne(prev, num, index):
    for p in primes[index:]:
        if checkWith(p, prev):
            if (num == 4):
                print(int(p) + sum([int(s) for s in prev]))
                return True
            else:
                if anotherOne(prev+[str(p)], num+1, index+1):
                    return True
        index += 1
    return False

anotherOne([], 0, 0)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")