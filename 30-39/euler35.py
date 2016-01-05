# Project Euler Problem 35
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Check all numbers (with set for already-tested)

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

# True if all members of the circle are prime
def isCirclePrime(lst):
    for n in lst:
        if not isPrimeMR(int(n)):
            return False
    return True

# generates the rotations of str number
def rotations(n):
    list = []
    for starti in range(len(n)):
        string = ''
        for readi in range(len(n)):
            string += n[(starti + readi)%len(n)]
        list.append(string)
    return list

tested = set()
count = 0 
cprimes = set()
for n in range(1, 1000000):
    # No need to check those already checked
    if n in tested:
        continue
    
    # Perform test
    areCircles = False
    rots = rotations(str(n))
    if isCirclePrime(rots):
        areCircles = True
    
    # Mark them as already tested
    # If circle primes add them
    for x in rots:
        if areCircles:
            cprimes.add(x)
        tested.add(x)
        
print(len(cprimes))
    

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
