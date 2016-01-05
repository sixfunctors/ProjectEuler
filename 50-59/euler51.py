# Project Euler Problem 51
# by Connor Halleck-Dube

import time
t0 = time.clock()

from primesmodule import isPrimeMR
from itertools import combinations

## Solution 1: Take every prime number in order and check every combination for a substitutionPrimes value of 8

# Checks a *-formatted number string to see how many primes it has
witnesses = [2, 3, 5]
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
def substitutionPrimes(string):
    if string.count('*') == 0:
        return isPrimeMR(int(string))
    l = string.split('*')
    count = 0
    if string[0] != '*' and isPrimeMR(int('0'.join(l))): # skip zero if the string begins with an *
        count += 1
    for d in digits:
        if isPrimeMR(int(d.join(l))):
            count += 1
    return count

# Test each combination of replaceable indices
found = False
n = 3
while not found:
    if not isPrimeMR(n):
        n +=2
        continue

    s = str(n)
    for l in range(1, len(s)):
        for indexlist in combinations(range(len(s)), l):
            digitlist = list(s)
            for i in indexlist:
                digitlist[i] = '*'
            template = ''.join(digitlist)
            if substitutionPrimes(template) >= 8:
                if template[0] == '*':
                    print('1'.join(template.split('*')))
                else:
                    print('0'.join(template.split('*')))
                found = True
                break
    
    n += 2
    

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
