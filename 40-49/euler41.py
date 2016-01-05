# Project Euler Problem 41
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Full iteration

INTMAX = 10000000

# Miller-Rabin Primality
witnesses = [2, 3, 5, 7, 11] # accurate for n < 2 152 302 898 747
def isPrimeMR(n):
    if (n == 2):
        return True
    elif (n <= 1) or (n%2 == 0):
        return False
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

# Returns true if number is pandigital
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
def isPandigital(n):
    s = str(n)
    return (sorted(list(s)) == digits[:len(s)])
    
# Iteration
largest = 0
for n in range(1, INTMAX):
    if isPandigital(n) and isPrimeMR(n):
        largest = n
print(largest)
        

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
