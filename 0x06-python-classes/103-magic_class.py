#!/usr/bin/python3
"""Magic class """
import math


class MagicClass:
    """
    my magic class body
    """
    def __init__(self, radius=0):
        """ setting up the magic class"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """
        calculating the area
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """
        get the circumfrence
        """
        return 2 * math.pi * self._MagicClass__radius
