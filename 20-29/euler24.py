# Project Euler Problem 24
# by Connor Halleck-Dube

import time
t0 = time.clock()

import itertools

## Solution 1: Pythonic

count = 0
for x in itertools.permutations(range(10)):
    count += 1
    if (count == 1000000):
        string = ""
        for d in x:
            string += str(d)
        print(string)
        break

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")