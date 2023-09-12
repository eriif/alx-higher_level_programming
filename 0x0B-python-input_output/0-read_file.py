#!/usr/bin/python3
"""Defines a text file reading func"""


def read_file(filename=""):
    """
    Print the contents of txt file to stdout
    """
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
