#! /usr/bin/env python

import random

start = []

for i in range(10):
    start.append(random.randint(0,1))

print start

def next_row(start_row):
    next_row = [0]*len(start_row)
    for each in enumerate(start_row):
        index, value = each
        try:
            if (start_row[index] == 0) and (start_row[index+1] == 0):
                next_row[index] = random.randint(0,1)
        except IndexError:
            if (start_row[index] == 0) and (start_row[0] == 0):
                next_row[index] = random.randint(0,1)
    return next_row

grid = [start]
grid.append(next_row(start))
i = 1
while i < len(start):
    grid.append(next_row(grid[1]))
    i = i + 1

for row in grid:
    print row
