# Project Euler Problem 29
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Python Sets

powers = set()

for a in range(2, 101):
    for b in range(2, 101):
        powers.add(a**b)
print(len(powers))

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")