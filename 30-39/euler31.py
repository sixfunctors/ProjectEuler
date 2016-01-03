# Project Euler Problem 31
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Recursion

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def coinCount(amount, cindex):
    if (amount == 0):
        return 1
    if (amount < 0) or (cindex < 0):
        return 0
    else:
        return (coinCount(amount, cindex-1) + coinCount(amount - coins[cindex], cindex))

print(coinCount(200, 7))

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
