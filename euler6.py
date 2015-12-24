# Project Euler Problem 6
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Naive Solution
ssquare = 0
for i in range(1, 101):
    ssquare += i*i

sum = 0
for i in range(1, 101):
    sum += i

print(sum*sum - ssquare)
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")