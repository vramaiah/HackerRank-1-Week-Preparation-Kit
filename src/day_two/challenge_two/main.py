#!/bin/python3

import os
import math

# Complete the 'diagonal_difference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonal(matrix, n):
    """
    Returns the sum of the numbers in the diagonal
    The diagonal starts in the upper right corner of matrix
    """
    sum = 0
    for i in range(n):
        row = matrix[i]
        sum += row[i]
    return sum


def diagonal_difference(matrix):
    """
    Finds the positive difference of diagonal sums
    The diagonal sum is the sum of the numbers a diagonal
    The diagonal starts in the upper right or upper left corner of matrix
    """
    n = len(matrix)
    diagonal_1 = diagonal(matrix, n)
    matrix.reverse()
    diagonal_2 = diagonal(matrix, n)
    return abs(diagonal_1 - diagonal_2)
    

# HackerRank Boilerplate
if __name__ == '__main__':
    path = os.environ.get('OUTPUT_PATH', 'output.txt')
    fptr = open(path, 'w')
    dimensions = int(input().strip())
    matrix = []
    for _ in range(dimensions):
        matrix.append(list(map(int, input().rstrip().split())))
    result = diagonal_difference(matrix)
    fptr.write(str(result) + '\n')
    fptr.close()
