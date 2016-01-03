# Project Euler Problem 26
# by Connor Halleck-Dube

import time
t0 = time.clock()

import decimal

## Solution 1: Iterative (Too long, but works)
"""
REPEATS = 4 # Needs to be larger than the largest subrepetition in any decimal expansion
decimal.getcontext().prec = 1000*REPEATS

# Truncates the reciprocal of d to n decimal places (returns integer x10**n)
def nRecipTrunc(d, n):
    recipf = 1/decimal.Decimal(d)
    return int(recipf*(10**n))
    
# generates a number like 1001001 and multiplies by the candidate cycle
def candidategen(cycle, period, repeats):
    sum = 0
    for times in range(repeats):
        sum += 10**(period*times)
    return (sum*cycle)
    
def period(d):
    declen = 1 #length of the decimal to check for cycling
    while True:
        dec = nRecipTrunc(d, declen) #trucated value
        for p in range(1, declen//REPEATS + 1):
            cycle = dec%(10**p)
            cand = candidategen(cycle, p, REPEATS)
            if ((dec - cand)%(10**(REPEATS*p )) == 0):
                return p
        
        declen += REPEATS

pmax = 0
value = 0
for d in range(1, 1000):
    p = period(d)
    print(d, p)
    if (p > pmax):
        pmax = p
        value = d

print(value)
"""
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")

## Solution 2: p-1 assumption
# If 10 is a primitive root mod p and p is prime, then period(p) = p-1
# This solution (correctly) assumes that our largest value will be some such number

# Miller-Rabin Primality
witnesses = [2, 3, 5] # accurate for n < 25 326 001
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

#Tests whether n is a primitive root of p
def isPrimitiveRoot(n, p):
    npowers = set()
    for order in range(1, p):
        power = (n**(order))%p
        if power in npowers:
            return False
        else:
            npowers.add(power)
            
    return True

primes = []
for d in range(3, 1000, 2):
    if isPrimeMR(d):
        primes.append(d)
primes.reverse()

for p in primes:
    if isPrimitiveRoot(10, p):
        print(p)
        break

## End Solution 2

t2 = time.clock()
print("Solution 2 took:", round(t2-t1, 4), "seconds.")