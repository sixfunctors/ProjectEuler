# Project Euler Problem 23
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Generate all abundant numbers less than 28123

amax = 28123

def isAbundant(n):
    l = []
    for d in range(1, int(sqrt(n))+1):
        if (n%d == 0):
            if (d != 1):
                l.append(n//d)
            l.append(d)
    if (sum(set(l)) > n):
        return True
    else:
        return False

# generate abundant list
abundlist = set()
for i in range(1, amax+1):
    if isAbundant(i):
        abundlist.add(i)

# check which can be expressed as sum of abundant numbers

def isAbundSum(n):
    for a in abundlist:
        if (n-a) in abundlist:
            return True
    return False

sum = 0
for i in range(1, amax+1):
    if not isAbundSum(i):
        sum += i

print(sum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")