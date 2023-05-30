#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """square"""
    def __init__(self, size=0):
        """initialise new square.

        Args:
            size(int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """get size of sqaure"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of square"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """define =="""
        return self.area() == other.area()

    def __ne__(self, other):
        """define !="""
        return self.area() != other.area()

    def __gt__(self, other):
        """define >"""
        return self.area() > other.area()

    def __lt__(self, other):
        """define <"""
        return self.area() < other.area()

    def __le__(self, other):
        """define <="""
        return self.area() <= other.area()

    def __ge__(self, other):
        """define >="""
        return self.area() >= other.area()
