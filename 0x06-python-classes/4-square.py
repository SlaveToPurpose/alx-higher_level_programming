#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """square."""
    def __init__(self, size=0):
        """initialise new square.

        Args:
            size(int): size of new square.
        """
        self.__size = size

    @property
    def size(self):
        """get size of sqaure"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of sqaure"""
        ret_area = self.__size ** 2
        return ret_area
