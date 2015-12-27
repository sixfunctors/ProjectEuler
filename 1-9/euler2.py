# Project Euler Problem 2
# by Connor Halleck-Dube

a = 0
b = 1
x = 0

while (b<4000000):
    if (b%2 == 0):
        x += b
    
    # Next values in fib sequence
    old = b
    b = a+b
    a = old
    
print(x)
