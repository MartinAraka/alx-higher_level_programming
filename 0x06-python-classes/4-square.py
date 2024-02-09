#!/usr/bin/python3

"""Defines a square"""


class Square:
    """
    A class that defines a square
    """
    def __init__(self, size):
        """
        A function that initialises a class square
        Args:
        size (int): The side of the square
        """
        self.size = size

    def area(self) -> int:
        """Returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self) -> int:
        """
        Retrieves the size of the square

        Returns:
        int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets or updates the size of the square

        Args:
            size (int): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
