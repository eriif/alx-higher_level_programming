#!/usr/bin/python3
"""
Defines an inherited list class Mylist
"""


class MyList(list):
    """
    Implements sorted printing for the built_in list class
    """
    pass

    def print_sorted(self):
        """
        Method that prints a sorted list in ascending
        """

        print(sorted(list(self)))
