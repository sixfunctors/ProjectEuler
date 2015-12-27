# Project Euler Problem 18
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Recursive solution via trees
string = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# Tree data structure
class node:
    value = 0
    children = []
    
    def __init__(self, value, childlist):
        self.children = childlist
        self.value = value

# converts the triangle into a grid
def toGrid(s):
    lines = s.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].split()
    return lines

# converts the grid into a tree
def toTree(grid, y, x):
    if (y+1 == ymax):
        return node(int(grid[y][x]), [])
    else:
        return node(int(grid[y][x]), [toTree(grid, y+1, x), toTree(grid, y+1, x+1)])
    
# finds the maximum path
def maxTree(tre):
    if (tre.children == []):
        return tre.value
    else:
        max = 0
        for child in tre.children:
            cmax = maxTree(child)
            if (cmax > max):
                max = cmax
        return (tre.value + max)
        

# execution
grid = toGrid(string)
ymax = len(grid)
print(maxTree(toTree(grid, 0, 0)))

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")