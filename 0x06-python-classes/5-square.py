#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        ret_area = self.__size ** 2
        return ret_area

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print('')
        if self.__size == 0:
            print('')
