# Project Euler Problem 22
# by Connor Halleck-Dube

import time
t0 = time.clock()

import names
import locale
from functools import cmp_to_key

## Solution 1: Locale sorting
 
def namesum(string):
    s = 0
    for d in string:
        s += (ord(d)-64)
    return s

index = 1
sum = 0

for name in sorted(names.nameslist, key = cmp_to_key(locale.strcoll)):
    sum += index*namesum(name)
    index += 1
    
print(sum)



## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")