#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """square."""
    def __init__(self, size):
        """initialise new square.

        Args:
            size(int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """get size of sqaure"""
        return self.__size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of sqaure"""
        ret_area = self.__size ** 2
        return ret_area

    def my_print(self):
        """print square using #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print('')
        if self.__size == 0:
            print('')
