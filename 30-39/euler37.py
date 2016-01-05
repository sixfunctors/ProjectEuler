# Project Euler Problem 31
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: 

# Miller-Rabin Primality
witnesses = [2, 3, 5, 7, 11] # accurate for n < 2 152 302 898 747
def isPrimeMR(n):
    if (n <= 1) or (n%2 == 0):
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
                break # this a is not a witness
        if poswitness: # a is a witness for n
            return False
    return True

lrprimes = set([2, 3, 5, 7])
def islrPrime(n):
    if (n in lrprimes):
        return True
    l = len(str(n))
    if (l == 1):
        return False
    s = str(n)[1:]
    if (isPrimeMR(n) and islrPrime(int(s))):
        lrprimes.add(n)
        return True
    return False

rlprimes = set([2, 3, 5, 7])
def isrlPrime(n):
    if (n in rlprimes):
        return True
    l = len(str(n))
    if (l == 1):
        return False
    s = str(n)[:l-1]
    if (isPrimeMR(n) and isrlPrime(int(s))):
        rlprimes.add(n)
        return True
    return False



# test candidates
sum = 0
for s in range(11, 1000000, 2):
    if islrPrime(s) and isrlPrime(s):
        sum += int(s)
print(sum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
