#!/usr/bin/python3

"""

This module defines class Rectangle, its area and perimeter and prints it

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
        """Returns the height of object of class Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """

        Sets height of object of class Rectangle

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of object of class Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter of object of class Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """string method for object of class Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        result = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                result += "#"
            if i < self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """returns officical string for oject of class Rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """deletes object of class rectangle"""
        print("Bye rectangle...")
