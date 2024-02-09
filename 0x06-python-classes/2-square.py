#!/usr/bin/python3


"""A class defining a square"""


class Square:
    """A class defining a square"""
    def __init__(self, size=0):
        """
        Constructs a square
        Args:
        size (int): The side of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
