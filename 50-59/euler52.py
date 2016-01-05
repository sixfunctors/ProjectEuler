# Project Euler Problem 52
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: 

# Checks whether the number has the same digits as multiplier*n
def compareDigits(n, multiplier):
    return sorted(list(str(n))) == sorted(list(str(n*multiplier)))
    
# 
def multIterate(n):
    for m in range(2, 7):
        if not compareDigits(n, m):
            return False
    return True
    
n = 1
while True:
    if multIterate(n):
        print(n)
        break
    
    n += 1

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
