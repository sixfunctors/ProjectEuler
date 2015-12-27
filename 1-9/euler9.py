# Project Euler Problem 9
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import sqrt

## Solution 1: sqrt(a^2 + b^2) + a + b 
found = False
prod = 0
for a in range(1, 1001):
    for b in range(a, 1001):
        c = sqrt(a**2 + b**2)
        if (a + b + c == 1000):
            found = True
            prod = int(a*b*c)
            print(a, b, c)
            
        if found: 
            break
    if found:
        break

print(prod)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")