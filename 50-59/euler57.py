# Project Euler Problem 57
# by Connor Halleck-Dube

import time
t0 = time.clock()

from fractions import Fraction
from decimal import Decimal

## Solution 1: Keep partial sums in a list (avoid recursion overload)

# Generates the nth iteration of the expansion for sqrt(2)
gensteps = [Fraction('2')]
def generate(n):
    def genstep(n):
        if len(gensteps) > n:
            return gensteps[n]
        else:
            f = Fraction(2)+Fraction(1)/genstep(n-1)
            gensteps.append(f)
            return f
    return Fraction(1) + Fraction(1)/genstep(n-1)

count = 0
for i in range(1, 1001):
    f = generate(i)
    if len(str(f.numerator)) > len(str(f.denominator)):
        count += 1
print(count)
    
## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
