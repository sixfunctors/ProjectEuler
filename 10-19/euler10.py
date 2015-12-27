# Project Euler Problem 10
# by Connor Halleck-Dube

import time
t0 = time.clock()


## Solution 1: Probabilistic primality test with reliable witnesses
# sufficient witnesses for all n < 25 326 001
witnesses = [2, 3, 5]

# Miller-Rabin
def isPrimeMR(n):
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
    
sum = 2
for i in range(3, 2000001, 2):
    if isPrimeMR(i):
        sum+=i

print(sum)
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")