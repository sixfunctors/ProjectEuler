# Project Euler Problem 38
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: 

INTMAX = 10000

# Tests if 1-9 pandigital
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
def is9Pandigital(n):
    lst = sorted(list(n))
    if (lst == digits):
        return True
    else:
        return False

# Generates a concatenated product
def conProd(n, maxd):
    string = ''
    d = 1
    while (d <= maxd):
        string += str(n*d)
        d += 1
    return string

panDigConProds = []
for n in range(1, INTMAX):
    strprod = ''
    d = 1
    while (len(strprod) < 9):
        d += 1
        strprod = conProd(n, d)
    if (is9Pandigital(strprod)):
        panDigConProds.append(strprod)
panDigConProds.sort()
print(panDigConProds[-1])

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
