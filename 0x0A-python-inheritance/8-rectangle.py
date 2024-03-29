#!/usr/bin/python3
"""
Module for a class Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle clasee herencia from BaseGeometry
    """
    def __init__(self, width, height):
        """
        init constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
