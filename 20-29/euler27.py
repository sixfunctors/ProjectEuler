# Project Euler Problem 27
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Miller-Rabin (Naive iteration)

# Miller-Rabin Primality
witnesses = [2, 3, 5] # accurate for n < 25 326 001
def isPrimeMR(n):
    if (n <= 1):
        return False
    elif (n == 2):
        return True
    
    s = 0
    d = n - 1
    while (d%2 == 0):
        d //= 2
        s += 1
    
    for a in witnesses:
        if (a >= n):
            continue
        
        if (pow(a, d, n) == 1):
            continue # this a is not a witness
        
        poswitness = True
        for r in range(0, s):
            if (pow(a, d*pow(2, r), n) == n-1):
                poswitness = False
                break #this a is not a witness
        
        if poswitness: # a is a witness for n
            return False
    
    return True

# returns the first value for which a quadratic formula with coefficients a and b doesnt return a prime number
def quadtest(a, b):
    n = 0
    val = n**2 + a*n + b
    while isPrimeMR(abs(val)):
        n += 1
        val = n**2 + a*n + b
    return n

quadmaxmax = 0
quadprod = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        quadmax = quadtest(a, b)
        if (quadmax > quadmaxmax):
            quadmaxmax = quadmax
            quadprod = a*b

print(quadprod)
        

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")