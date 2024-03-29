#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """square"""

    def __init__(self, size=0):
        """initialise new square.

        Args:
            size(int): size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return area of square."""
        ret_area = self.__size ** 2
        return ret_area
