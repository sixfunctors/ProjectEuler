# Project Euler Problem 20
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import factorial

## Solution 1: Naive Solution

def digitsum(x):
    if (x//10 == 0):
        return x%10
    else:
        return (x%10) + digitsum(x//10)

n = factorial(100)
print(digitsum(n))

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")