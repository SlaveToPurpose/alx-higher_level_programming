#!/usr/bin/python3
"""Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area"""
        return self.__height * self.__width

    def __str__(self):
        """print representation"""
        return "[{}] {:d}/{:d}".format(
            self.__class__.__name__, self.__width, self.__height)
