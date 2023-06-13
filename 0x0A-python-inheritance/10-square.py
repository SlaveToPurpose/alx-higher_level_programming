#!/usr/bin/python3
"""Square class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square definition"""

    def __init__(self, size):
        """Initialize a new square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """computes the area of the square"""
        return self.__size * self.__size
