# Project Euler Problem 2
# by Connor Halleck-Dube

a = 0
b = 1
sum = 0

while b<4000000:
    if (b%2 == 0):
        sum += b
    
    # Next values in fib sequence
    old = b
    b = a+b
    a = old
    
print(sum)