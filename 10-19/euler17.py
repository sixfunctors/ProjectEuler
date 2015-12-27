# Project Euler Problem 17
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1
digits = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
tens = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

# works for 1-999
def numstring(n):
    name = ""
    if (n == 0):
        return ""
    
    if (n >= 100) and (n<1000): # three-digit
        name += digits[n//100]
        name += ' hundred'
        if (n%100 != 0):
            name += ' and '
            name += numstring(n%100) 
        return name
        
    elif (n >= 10) and (n < 100): # two-digit
        if (n//10 == 1): # 10-19
            name += teens[n] 
            return name
        else: # 20+
            name += tens[n//10] 
            if (n%10 != 0):
                name += ' '
                name += numstring(n%10)
            return name
            
    elif (n < 10):
        return digits[n]
    else:
        return "ERROR"

list = ['one thousand']
sum = 11
for i in range(1, 1000):
    name = numstring(i)
    list.append(name)
    words = name.split()
    for word in words:
        sum += len(word)

print(list)
print(sum)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")