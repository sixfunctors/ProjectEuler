# Project Euler Problem 15
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import factorial

xmax = 20
ymax = 20

## Solution 1: Recursive paths - unreasonably long
"""
def paths(x, y):
    if (x+1 == xmax) and (y+1 == ymax):
        return 1
    elif (y+1 == ymax):
        return (paths(x+1, y))
    elif (x+1 == xmax):
        return (paths(x, y+1))
    else:
        return (paths(x, y+1) + paths(x+1, y))

print(paths(0, 0))
"""
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")

## Solution 2: Permutational Solution
# A path is written as a twenty-length string of l and d
# eg. 'ldldldldldldldldldld'
# Then the problem becomes nCr

answer = factorial(xmax+ymax) // (factorial(xmax)* factorial(ymax))
print(answer)

## End Solution 2

t2 = time.clock()
print("Solution 2 took:", round(t2-t1, 4), "seconds.")
