# Project Euler Problem 53
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Computation

# nCr by one method
def choose(n, r):
    prod = 1
    for i in range(1, r+1):
        prod *= (n+1-i)/i
    return int(round(prod))

count = 0
for n in range(1, 101):
    for r in range(n+1):
        if choose(n, r) > 1000000:
            count += 1
print(count)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
