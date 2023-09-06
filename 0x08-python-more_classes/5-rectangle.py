#!/usr/bin/python3

class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initialization of the class"""
        self.width = width
        self.height = height

    def __str__(self):
        """return a string """
        if self.__height == 0 or self.__width == 0:
            return ''
        _str = ''
        for x in range(self.__height):
            for y in range(self.__width):
                _str += '#'
            _str += '\n'
        return (rectangle_str[:-1])

    def __repr__(self):
        """ rectangle representation"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """delete the inst."""
        print("Bye rectangle...")

    @property
    def width(self):
        """get width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    """set height"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """prints area"""
        return self.__width * self.__height

    def perimeter(self):
        """prints the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__width + self.__height))
