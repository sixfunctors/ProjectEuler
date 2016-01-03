# Project Euler Problem 32
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import sqrt

## Solution 1: Checking all factor pairs

INTMAX = 10000
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is9Pandigital(mand, mult, prod):
    unionlist = list(str(mand) + str(mult) + str(prod))
    unionlist.sort()
    if (unionlist == digits):
        return True
    else:
        return False

def divisorpairs(n):
    l = []
    for d in range(1, int(sqrt(n))+1):
        if (n%d == 0):
            l.append((d, n//d))
    return l

sum = 0
for i in range(1, INTMAX):
    for pair in divisorpairs(i):
        if is9Pandigital(pair[0], pair[1], i):
            sum += i
            break
print(sum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
