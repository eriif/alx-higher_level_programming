#!/usr/bin/python3
""" Rectangle """


class Rectangle:
    """a class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ the instanciation """
        self.width = width
        self.height = height

    def __str__(self):
        """ returns the string rep"""
        if self.__height == 0 or self.__width == 0:
            return ''
        _str = ''
        for x in range(self.__height):
            for y in range(self.__width):
                _str += '#'
            _str += '\n'
        return (_str[:-1])

    @property
    def width(self):
        """gets the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the hight"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the hight """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area calculation """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter calculation """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__width + self.__height))
