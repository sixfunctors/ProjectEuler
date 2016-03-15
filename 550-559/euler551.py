# Project Euler Problem 551
# by Connor Halleck-Dube

import time
t0 = time.clock()


## Solution 1: Naive Solution

def sumDigits(s):
    return sum([int(d) for d in s])

def sumDigitsn(n):
    sum = 0
    while (n//10):
        sum += n%10
        n //= 10
    return sum + (n%10)
    
def nexta(a, i):
    for times in range(0, i):
        a += sumDigitsn(a)
    return a
        

seq = {}
diff = {}
i = 10**6
seq[i] = 31054319
jump = 10**6
i += jump
while (i < 10**15):
    seq[i] = nexta(seq[i-jump], jump)
    
    diff[i] = seq[i]-seq[i-jump]
    print(diff[i])
    
    i += jump
     


## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")