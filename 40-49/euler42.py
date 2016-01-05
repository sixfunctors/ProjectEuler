# Project Euler Problem 42
# by Connor Halleck-Dube

import time
t0 = time.clock()

import words

## Solution 1: Pre-generate triangle numbers

TRIMAX = 1000

# calculates the value of a word
def value(word):
    sum = 0
    for c in word:
        sum += ord(c)-ord('A')+1
    return sum

# triangle number generator
def tri(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

# generate first 1000 triangle numbers
triangles = set()
for n in range(1, TRIMAX):
    triangles.add(tri(n))

# count triangle words
count = 0
for word in words.words:
    if value(word) in triangles:
        count += 1
print(count)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")