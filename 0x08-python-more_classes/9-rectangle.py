#!/usr/bin/python3
"""defintion for Rectangle"""


class Rectangle:
    """Rectangle called class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, widthval):
        """setter for width"""
        if type(widthval) is not int:
            raise TypeError("width must be an integer")
        if widthval < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthval

    @property
    def height(self):
        """getter for height"""
        return (self.__height)

    @height.setter
    def height(self, heightval):
        """setter for height"""
        if type(heightval) is not int:
            raise TypeError("height must be an integer")
        if heightval < 0:
            raise ValueError("height must be >= 0")
        self.__height = heightval

    def area(self):
        """calculate area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate perimeter of rectangle"""
        if self.__width == 0:
            return (0)
        elif self.__height == 0:
            return (0)
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """printing rectangle in #s"""
        rectAngle = ""
        if self.__width == 0 or self.__height == 0:
            return (rectAngle)
        symbolz = str(self.print_symbol)
        for i in range(self.__height):
            rectAngle += "{}".format(symbolz * self.__width)
            if i != (self.__height - 1):
                rectAngle += "\n"
        return (rectAngle)

    def __repr__(self):
        """internal representation of rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return biggest rectangle based on are"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method to return new Rectangle instance"""
        return cls(size, size)
