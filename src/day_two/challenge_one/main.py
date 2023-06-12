#!/bin/python3

import os

# Complete the 'lonely_integer' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def lonely_integer(array):
    integers = set(array)
    for integer in integers:
        if array.count(integer) == 1:
            return integer

# HackerRank generated boilerplate
if __name__ == '__main__':
    path = os.environ.get('OUTPUT_PATH', 'output.txt')
    fptr = open(path, 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonely_integer(a)
    fptr.write(str(result) + '\n')
    fptr.close()
