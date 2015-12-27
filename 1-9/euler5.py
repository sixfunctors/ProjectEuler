# Project Euler Problem 5
# by Connor Halleck-Dube

from functools import reduce
import time
t0 = time.clock()

## Solution 1: Product of prime factors
divisors = range(2, 21)
factors = []
product = 1

# prime factors of a number with repeats
def factor(n):
    l = []
    value = n
    while (value > 1):
        for d in range(2, int(value)+1):
            if (value%d == 0):
                value /= d
                l.append(d)
                break
    return l

for divisor in divisors:
    factors.append(factor(divisor))

# finds the max times each divisor appears in the answer
# the product of these is the answer
for divisor in divisors:
    count = 0
    for fact in factors:
        appears = fact.count(divisor)
        if appears>count:
            count = appears
    product *= divisor**count

print(product)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 3), "seconds.")
    