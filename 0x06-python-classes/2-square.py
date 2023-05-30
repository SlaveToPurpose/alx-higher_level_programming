#!/usr/bin/python
class Square:
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be >= 0")
        self.__size = size
