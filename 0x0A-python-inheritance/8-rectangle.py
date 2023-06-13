#!/usr/bin/python3
'''A module for working with geometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """geometry obj"""

    def __init__(self, width, height):
	'''Initializes Rectangle
	Args:
	    width (int): The width of the rectangle.
	    height (int): The height of the rectangle.
	'''

		self.integer_validator('width', width)
		self.integer_validator('height', height)

		self.__width = width
		self.__height = height
