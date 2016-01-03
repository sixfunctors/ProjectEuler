# Project Euler Problem 28
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: The largest diagonal is side^2

def spiralSum(side):
    if (side == 1):
        return 1
    else:
        return (4*side**2 - 6*(side-1) + spiralSum(side-2))
        
print(spiralSum(1001))

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")