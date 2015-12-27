# Project Euler Problem 19
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Logical Analysis

# let our day count begin on jan 1st, 1901, which was a Tuesday. let Tuesday = 0. Thus 
sunday = 5

# a sunday will be any day number d satisfying d%7 == 6
# let jan 1st be indexed 0. Thus, jan 1st = 0, feb 1st = 31, etc
firsts = [ 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334 ]
lfirsts = [ 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335 ]

# generate 4 year cycle
firsts4 = []
for i in range(3):
    for item in firsts:
        firsts4.append(i*365+item)
for item in lfirsts:
    firsts4.append(3*365+item)
    
# days in a century
daymax = int(365.25*100)

# iterate
count = 0
for i in range(daymax):
    if (i%1461 in firsts4) and (i%7 == sunday):
        count += 1

print(count)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")