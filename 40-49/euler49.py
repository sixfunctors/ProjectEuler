# Project Euler Problem 49
# by Connor Halleck-Dube

import time
t0 = time.clock()

from primesmodule import isPrimeMR

## Solution 1: Straightforward iteration


    
# Checks whether the three numbers are permutations of each other
def sameDigits(s, s2, s3):
    l = sorted(list(s))
    if (l == sorted(list(s2))) and (l == sorted(list(s3))):
        return True
    else:
        return False

for n in range(1488, 10000):
    n2 = n + 3330
    n3 = n + 6660
    if isPrimeMR(n) and isPrimeMR(n2) and isPrimeMR(n3) and sameDigits(str(n), str(n2), str(n3)):
        print(str(n) + str(n2) + str(n3))
        

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
