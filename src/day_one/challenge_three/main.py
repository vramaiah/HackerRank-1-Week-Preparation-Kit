#!/bin/python3

import os

# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def time_conversion(time_12hr):
    # parses time
    time_12hr = time_12hr.strip()
    (hours, minutes, seconds) = map(int, time_12hr[:-2].split(':'))
    suffix = time_12hr[-2:]
    # Does 12 hr --> 24 hr conversion
    if (suffix == 'PM') and (hours != 12):
        hours += 12
    if (suffix == 'AM') and (hours == 12):
        hours = 0
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    

if __name__ == '__main__':
    path = os.environ.get('OUTPUT_PATH', 'output.txt')
    fptr = open(path, 'w')
    s = input()
    result = time_conversion(s)
    fptr.write(result + '\n')
    fptr.close()
