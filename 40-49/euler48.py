# Project Euler Problem 48
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Compute full value

sum = 0
for i in range(1, 1000):
    sum += i**i
s = str(sum)
print(s[len(s)-10:len(s)])

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
