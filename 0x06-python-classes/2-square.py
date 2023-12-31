#!/usr/bin/python3
"""a class that defines a square """


class Square:
    """
    Square class body
    """

    def __init__(self, size=0):
        """
        set the Square class attributes
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
