# Project Euler Problem 55
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Manual Testing

# One iteration of reverse-adding
def reverseSum(n):
    return n + int(str(n)[::-1])

def isPalindrome(n):
    return str(n) == str(n)[::-1]

# Performs reverse-sum 50 times.
def isLychrel(n):
    for times in range(50):
        n = reverseSum(n)
        if isPalindrome(n):
            return False
    return True

count = 0
for n in range(1, 10000):
    if isLychrel(n):
        count += 1
print(count)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
