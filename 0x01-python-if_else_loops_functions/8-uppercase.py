#!/usr/bin/python3
# 8-uppercase.py


def uppercase(input_str):
    """Print a string in uppercase."""
    r = ""


for char in input_str:
    if 'a' <= char <= 'z':
        offset = ord('A') - ord('a')
        r += chr(ord(char) + offset)
    else:
        r += char
        print(r)
