# Project Euler Problem 25
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Naive solution
a = 0
b = 1
index = 1

while (len(str(b)) < 1000):
    # Next values in fib sequence
    old = b
    b = a+b
    a = old
    index += 1
    
print(index)


## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")