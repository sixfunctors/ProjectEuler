# Project Euler Problem 39
# by Connor Halleck-Dube

import time
t0 = time.clock()

from math import sqrt

## Solution 1: Math Derivation
# Beginning w Pythagorean Theorem and perimeter, derived expression for b(a)
# a^2 + b^2 = c^2 and
# a + b + c = p
# ==>
# b = (p^2 - 2pa)/(2(p - a))


# Returns the number of integral solutions as a function of p
def rightTriangleSolutions(p):
    lst = set()
    for a in range(1, p//2 + 1):
        b = (p**2 - 2*p*a)/(2*(p-a))
        if (b > a) and (b.is_integer()):
            lst.add((a, b, sqrt(a**2 + b**2)))
    return len(lst)

maxsol = 0
maxp = 0
for p in range(1, 1001):
    sol = rightTriangleSolutions(p)
    if (sol > maxsol):
        maxsol = sol
        maxp = p
print(maxp)
    
    

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
