# Project Euler Problem 14
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Naive Solution (iterate through starting points)
"""
def collatzn(num):
    i = 0 
    n = num
    while (n != 1):
        i += 1
        if (n%2 == 0):
            n //= 2
        else:
            n = 3*n + 1
    
    return i

collmax = 0
value = 0
for n in range(1, 1000000):
    coll = collatzn(n)
    if (coll > collmax):
        collmax = coll
        value = n

print(value)
"""
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")

## Solution 2: Dictionary Generation
Collatz = {1:4, 4:2, 2:1}

def Colladd(num):
    n = num
    while not (n in Collatz):
        if (n%2 == 0):
            Collatz[n] = n//2
            n //= 2
        else:
            Collatz[n] = 3*n + 1
            n = 3*n + 1

collmax = 0
value = 0
for num in range(1, 1000000):
    if not (n in Collatz):
        Colladd(n)
    
    n = num
    i = 0
    while (n != 1):
        i += 1
        n = Collatz[n]
    
    # new longest chain found
    if (i > collmax):
        collmax = i
        value = num
        
print(value)


## End Solution 2

t2 = time.clock()
print("Solution 2 took:", round(t2-t1, 4), "seconds.")