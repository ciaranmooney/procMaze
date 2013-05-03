#! /usr/bin/env python

import random

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

def create_maze(size):
    start = []

    for i in range(size):
        start.append(random.randint(0,1))

    grid = [start]
    grid.append(next_row(start))
    i = 1
    while i < len(start):
        grid.append(next_row(grid[1]))
        i = i + 1

    return grid

maze = create_maze(10)

for row in maze:
    print(row)

