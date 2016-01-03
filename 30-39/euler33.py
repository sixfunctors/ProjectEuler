# Project Euler Problem 33
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Check all pairs

pairs = []
for d in range(11, 99):
    for n in range(11, d):
        num = str(n)
        den = str(d)
        if (num[0] == den[1]):
            if (num[1] == '0') or (den[0] == '0'):
                continue
            newn = int(num[1])
            newd = int(den[0])
            
            if (n/d == newn/newd):
                pairs.append((n, d))
        elif (num[1] == den[0]):
            if (num[0] == '0') or (den[1] == '0'):
                continue
            newn = int(num[0])
            newd = int(den[1])
            
            if (n/d == newn/newd):
                pairs.append((n, d))
                
numprod = 1
denprod = 1
for pair in pairs:
    numprod *= pair[0]
    denprod *= pair[1]
print(denprod//numprod) # this only works because the numerator is a factor of the denominator. 
# Makes fraction simplification easier

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")

