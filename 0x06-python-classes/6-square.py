#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """square."""
    def __init__(self, size=0, position=(0, 0)):
        """initialise new square.

        Args:
            position(int, int): position of new square
            size(int): size of new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get position of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate and return area of sqaure"""
        return (self.__size ** 2)

    def my_print(self):
        """print square using #"""
        if self.__size == 0:
            print('')
            return

        for i in range(self.__position[1]):
            print('')

        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print('')
