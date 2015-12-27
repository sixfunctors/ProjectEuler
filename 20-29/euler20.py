# Project Euler Problem 20
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Naive Solution

string = str(2**1000)
sum = 0
for d in string:
    sum += int(d)
print(sum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")