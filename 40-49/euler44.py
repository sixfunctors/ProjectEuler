# Project Euler Problem 44
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Pregenerate INDEXMAX pentagonal numbers

INDEXMAX = 10000

# nth pentagonal number
def pent(n):
    return (n*(3*n-1))//2

# Generate pentagonal numbers and compare to all previous
pentagonals = set()
for n in range(1, INDEXMAX):
    pentagonals.add(pent(n))

diffmin = float("inf") #Starts infinite for comparisons
for j in pentagonals:
    for k in pentagonals:
        diff = j-k
        if diff == 0:
            continue
        sum = j+k
        if (diff in pentagonals) and (sum in pentagonals) and (diff < diffmin):
            diffmin = diff
print(diffmin)
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
