# Project Euler Problem 31
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Naive Iteration

def isPalindromeString(s):
    return (s[::-1] == s)
    
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]
      

sum = 0
for n in range(1, 1000000):
    if isPalindromeString(toStr(n, 2)) and isPalindromeString(toStr(n, 10)):
        sum += n
print(sum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
