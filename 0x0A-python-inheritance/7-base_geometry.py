#!/usr/bin/python3
"""A module that contains the BaseGeometry class"""


class BaseGeometry:
    """base class for all objects"""

    def area(self):
        """calculate the area"""
        
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
