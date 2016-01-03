# Project Euler Problem 30
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Naive Solution (Cap set at 500000)

FIFTHMAX = 500000

def fifthPowerSum(n):
    sum = 0
    for d in str(n):
        sum += int(d)**5
    if (sum == n):
        return True
    return False

fpsum = 0
for n in range(2, FIFTHMAX):
    if fifthPowerSum(n):
        fpsum += n
print(fpsum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")