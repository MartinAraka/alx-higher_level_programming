#!/usr/bin/python3
"""
class square has private instance size and public instance are
if size is not an integer raise type error
if size is less than 0 raise value error
"""


class Square:
    """
    takes in private instance size, private instance positions
    and public instance area
    """

    def __init__(self, size=0, position=(0, 0)):
        """define object size
        define object position"""
        self.__size = size
        self.position = position

    @property
    def position(self):
        """Get/self the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """check if position is a tuple of two positive integers"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        def area(self):
            """public instance attribute area.
            returns the value of the area of the square"""
            return (self.__size ** 2)

        def my_print(self):
            """print to stdout the square to the character #"""
            if self.__size == 0:
                print()
                return
            for y in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                print()
