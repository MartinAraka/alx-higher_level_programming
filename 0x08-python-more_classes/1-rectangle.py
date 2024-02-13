#!/usr/bin/python3

"""

This module contains a function that builds class Rectangle

"""


class Rectangle:
    """

    Defines a rectangle

    """
    def __init__(self, width=0, height=0):
        """

        Instantiates object of class Rectangle

        Args:
        width (int and optional): short side, defaults to 0
        height (int and optional): long side, defaults to 0

        Raises:
        TypeError: if length or width not an int
        ValueError: if length or width < 0

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of object of class Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """

        Sets width of object of class Rectangle

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """

        Sets height of object of class Rectangle

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
