#!/bin/python3

# Complete the 'plus_minus' function below.
# The function accepts INTEGER_ARRAY array as parameter.

def plus_minus(array, precision=6):
    length = len(array)
    positive = 0
    negitive = 0
    zero = 0
    for n in array:
        if n == 0:
            zero += 1
        elif n > 0:
            positive += 1
        else:
            negitive += 1
    for number in (positive, negitive, zero):
        number /= length
        print(f"{number:.{precision}f}")
      
if __name__ == '__main__':
    n = int(input().strip())
    array = list(map(int, input().rstrip().split()))
    plus_minus(array)
