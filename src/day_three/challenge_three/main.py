#!/bin/python3

import os

# Complete the 'caesar_cipher' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def caesar_cipher(message: str, shift: int):
    # Changes message to a list
    message = list(message)
    # Checks shift to make sure it does not exceed 26
    shift = shift % 26
    # Loops over all characters in the input message
    for i, char in enumerate(message):
        print(char)
        # Sets a variable, char_is_upper to true if the char is uppercase
        if char.isalpha():
            if char.isupper():
                char_is_upper = True
            else:
                char_is_upper = False
            # Finds the index of char in LETTERS
            index = LETTERS.index(char.lower())
            # Finds the new index of char in LETTERS
            index = ((index + 1 + shift) % 26) - 1
            # Replaces char in message
            char = LETTERS[index]
            if char_is_upper:
                char = char.upper()
            message[i] = char
    # Returns the message
    return ''.join(message)

# HackerRank boilerplate
if __name__ == '__main__':
    path = os.environ.get('OUTPUT_PATH', 'output.txt')
    fptr = open(path, 'w')
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesar_cipher(s, k)
    fptr.write(result + '\n')
    fptr.close()
