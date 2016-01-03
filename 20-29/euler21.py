# Project Euler Problem 21
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import factorial
from math import sqrt

## Solution 1: Simple amicable pair generation

def properdivisors(n):
    l = []
    for d in range(1, int(sqrt(n))+1):
        if (n%d == 0):
            if (d != 1):
                l.append(n//d)
            l.append(d)
    return l

pairs = set()
for a in range(3, 10000):
    b = sum(properdivisors(a))
    if (sum(properdivisors(b)) == a) and (a != b):
        pairs.add(a)
        pairs.add(b)

print(sum(pairs))
    

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")