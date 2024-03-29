#!/usr/bin/python
""" Inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__weight = weight
        self.__height = height
