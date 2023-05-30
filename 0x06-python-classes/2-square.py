#!/usr/bin/python
"""Defining a class Square"""


class Square:
    """square."""
    def __init__(self, size=0):
         """initialise new square.

        Args:
            size(int): size of new square.
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be >= 0")
        self.__size = size
