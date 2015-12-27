# Project Euler Problem 12
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import sqrt

## Solution 1: Naive Solution
def tri(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def factors(num):
    l = []
    n = num
    for d in range(1, int(sqrt(n))+1):
        if (n%d == 0):
            l.append(n//d)
            l.append(d)
    return l

i = 1
while True:
    n = tri(i)
    if (len(factors(n))>500):
        print(n)
        break
    
    i += 1
    
    
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")