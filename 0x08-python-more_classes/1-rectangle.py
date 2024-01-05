#!/usr/bin/python3
"""
Defining a class rectangle
"""


class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        """Get the width"""
        return self.__width

    def width(self, value):
        """the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """Get the height"""
        return self.__height

    def height(self, value):
        """The height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
