#!/bin/python3

# Complete the 'min_and_max_sum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def min_and_max_sum(array):
    total_sum = sum(array)
    min_sum = sum(array) - max(array)
    max_sum = sum(array) - min(array)
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    min_and_max_sum(arr)
