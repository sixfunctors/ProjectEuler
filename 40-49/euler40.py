# Project Euler Problem 40
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Naive Solution

# Generates constant string
champer = ''
i = 1
while (len(champer)<=1000000):
    champer += str(i)
    i += 1

# finds product of terms
prod = 1
exp = 0
while (exp < 7):
    prod *= int(champer[10**exp-1])
    exp += 1

print(prod)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
