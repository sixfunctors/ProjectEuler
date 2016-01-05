# Project Euler Problem 45
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Generate until you find one
# since hex(i) > pent(i) > tri(i), tri(i) == pent(j) == hex(k) implies that j and k are less than i.
# If we iterate by index and check tri(i), the other two will already have been generated

INDEXMAX = 100000

# nth triangle number
def tri(n):
    return n*(n+1)//2

# nth pentagonal number
def pent(n):
    return n*(3*n-1)//2

# nth hexagonal number
def hex(n):
    return n*(2*n-1)
    
pentagonals = set()
hexagonals = set()
foundone = False # because we actually want the second such number
for i in range(1, INDEXMAX):
    t = tri(i)
    if (t in pentagonals) and (t in hexagonals):
        if foundone:
            print(t)
            break
        else:
            foundone = True
    
    pentagonals.add(pent(i))
    hexagonals.add(hex(i))

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
