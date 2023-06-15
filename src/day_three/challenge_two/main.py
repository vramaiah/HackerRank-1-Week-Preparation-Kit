#!/bin/python3

import os

# Complete the 'tower_breakers' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m

def tower_breakers(n, m):
    # If there are an even number of towers of only one tower, P2 wins
    if n % 2 == 0 or m == 1:
        return 2
    # Otherwise, P1 wins
    else:
        return 1

# HackerRank boilerplate
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = tower_breakers(n, m)
        fptr.write(str(result) + '\n')
    fptr.close()
