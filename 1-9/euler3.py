# Project Euler Problem 3
# by Connor Halleck-Dube

factors = []
value = 600851475143
divisor = 1

while (divisor <= value) and (value != 1):
    if (value%divisor == 0):
        value = value/divisor
        factors.append(divisor)
    
    divisor += 1

#factors will automatically be ordered
print(factors[-1])