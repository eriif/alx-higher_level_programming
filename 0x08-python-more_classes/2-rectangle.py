#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initialize private attributes for width and height
        """
        self.__width = width
        self.__height = height

    @property
    """
    Getter method for width attribute
    """
    def width(self):
        return self.__width

    @property
    """
    Getter method for height attribute
    """
    def height(self):
        return self.__height

    @width.setter
    """
    Setter method for width attribute
    """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    """
    Setter method for height attribute
    """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
