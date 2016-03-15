# Project Euler Problem 59
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Check for occurrences of 'e'

# Returns whether there are the appropriate number of 'e's in the text
occurrence = 0.11
def check(plaintext):
    if (plaintext.count('e') >= occurrence*len(plaintext.replace(' ', ''))):
        return True
    else:
        return False

# Decodes list of ascii values with key
def decode(list, key):
    s = ''
    i = 0
    for letter in list:
        s += chr(letter ^ ord(key[i%3]))
        i += 1
    return s
    
# Generates keywords
alphabets = [chr(d) for d in range(97, 123)]
keywords = [''.join(i) for i in itertools.product(alphabets, repeat = 3)]

# Read the cipher
r = open('cipher.txt')

maxcheck = 0
maxdecoded = []
count = 0
for line in r:
    for key in keywords:
        list = [int(asc) for asc in line.split(',')]
        decoded = decode(list, key)
        if (check(decoded)):
            maxcheck = check(decoded)
            maxdecoded = decoded
        count += 1
        
print(sum([ord(char) for char in maxdecoded]))

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
