# Project Euler Problem 56
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Evaluate Digital Sums

def digitSum(n):
    return sum([int(d) for d in str(n)])

maxdsum = 0
for a in range(1, 100):
    for b in range(1, 100):
        dsum = digitSum(a**b)
        if dsum > maxdsum:
            maxdsum = dsum
print(maxdsum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
