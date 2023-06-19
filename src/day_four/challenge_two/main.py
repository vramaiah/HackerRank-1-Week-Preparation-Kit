#!/bin/python3

import os

# Complete the 'super_digit' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k

def super_digit(n: str, k: int):
    n2 = [int(d) for d in n]
    if len(n2) == 1:
        return n2[0]
    else:
        n_sum = sum(n2)
        return super_digit(str(n_sum*k), 1)

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = super_digit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
