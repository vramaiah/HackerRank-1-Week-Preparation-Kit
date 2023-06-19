#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'grid_challenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def grid_challenge(input_grid):
    grid = []
    for row in input_grid:
        row = list(row)
        row.sort()
        grid.append(row)
    columns = list(zip(*grid))
    columns = [list(column) for column in columns]
    is_sorted = True
    print(columns)
    for column in columns:
        sorted_column = sorted(column)
        if sorted_column != column:
            is_sorted = False
            print(column)
    if is_sorted:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        result = grid_challenge(grid)
        fptr.write(result + '\n')
    fptr.close()
