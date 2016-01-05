# Project Euler Problem 34
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import factorial

## Solution 1: Straightforward

INTMAX = 100000

def isCurious(n):
    sum = 0
    for d in str(n):
        sum += factorial(int(d))
    if (sum == n):
        return True
    else: 
        return False

cursum = 0
for n in range(3, INTMAX): # Problem excludes 1 and 2
    if isCurious(n):
        cursum += n
print(cursum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
