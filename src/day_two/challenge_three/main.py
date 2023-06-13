#!/bin/python3

import os

# Complete the 'counting_sort' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.

def counting_sort(array):
    """
    Makes list of the frequencies of each value from a list:
    The input list, array
    """
    result = [0 for n in range(100)]
    for element in array:
        result[element] += 1
    return result

# HackerRank Boilerplate
if __name__ == '__main__':
    path = os.environ.get('OUTPUT_PATH', 'output.txt')
    fptr = open(path, 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = counting_sort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
