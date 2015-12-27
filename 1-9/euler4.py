# Project Euler Problem 4
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Naive solution
a = 1000
b = 1000
palindromes = []

#checks all combinations naively
while a>100: 
    a -= 1
    while b>100:
        b -= 1
        prod = str(a*b)
        
        # palindrome test
        if (prod[::-1] == prod):
            palindromes.append(int(prod))
    
    b = 1000

palindromes = list(set(palindromes))
palindromes.sort()
print(palindromes[-1])
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 3), "seconds.")

## Solution 2: Pre-generates all (a, b) pairs
# generates pairs
pairs = set()
for a in range(100, 1000):
    for b in range(100, 1000):
        pairs.add((a, b))

# sorts the pairs by their sum
sortedpairs = sorted(list(pairs), key=lambda pair: (pair[0]+pair[1]))
sortedpairs.reverse()

# checks them in a more efficient order
for pair in sortedpairs:
    prod = str(pair[0]*pair[1])
    if (prod == prod[::-1]):
        print(int(prod))
        break
## End Solution 2

t2 = time.clock()
print("Solution 2 took:", round(t2-t1, 3), "seconds.")

## Solution 3: Pre-generates all products
products = set()
for a in range(100, 1000):
    for b in range(100, 1000):
        products.add(a*b)

sortedprods = sorted(list(products))
sortedprods.reverse()

for prod in sortedprods:
    if (str(prod) == str(prod)[::-1]):
        print(prod)
        break
## End Solution 3

t3 = time.clock()
print("Solution 3 took:", round(t3-t2, 3), "seconds.")

