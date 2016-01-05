# Project Euler Problem 43
# by Connor Halleck-Dube

import time
t0 = time.clock()

import itertools

## Solution 1: Pregenerate Pandigital numbers

# Generate 0-9 Pandigital numbers
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pandigitals = set()
for l in itertools.permutations(digits):
    s = ''.join(list(l))
    if s[0] == '0':
        continue
    pandigitals.add(s)

# tests substring beginning with index i for divisibility with the i-1 th prime
primes = [2, 3, 5, 7, 11, 13, 17]
def isSubDiv(string, i):
    return int(string[i:i+3])%primes[i-1] == 0
    
# Tests the string all 7 times
def isSubDivIter(string):
    for i in range(1, 8):
        if not isSubDiv(string, i):
            return False
    return True
    
# Iteration
sum = 0
for pan in pandigitals:
    if isSubDivIter(pan):
        sum += int(pan)
print(sum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
