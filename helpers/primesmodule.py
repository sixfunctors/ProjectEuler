## Primesmodule
# Contains functions for primacy testing

# Miller-Rabin Primality
witnesses = [2, 3, 5, 7, 11] # accurate for n < 2 152 302 898 747
def isPrimeMR(n):
    if (n == 2):
        return True
    elif (n <= 1) or (n%2 == 0):
        return False
    s = 0
    d = n - 1
    while (d%2 == 0):
        d //= 2
        s += 1
    
    for a in witnesses:
        if (a >= n):
            continue
        if (pow(a, d, n) == 1):
            continue # this a is not a witness
        poswitness = True
        for r in range(0, s):
            if (pow(a, d*pow(2, r), n) == n-1):
                poswitness = False
                break # this a is not a witness
        if poswitness: # a is a witness for n
            return False
    return True