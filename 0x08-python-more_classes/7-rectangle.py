#!/usr/bin/python3
"""defintion for Rectangle"""


class Rectangle:
    """Rectangle called class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialise rectangle"""

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width"""

        return self.__width

    @width.setter
    def width(self, width):
        """setter for width"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """getter for height"""

        return (self.__height)

    @height.setter
    def height(self, height):
        """setter for height"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

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
            rectAngle += symbolz * self.__width
            if i != self.__height - 1:
                rectAngle += "\n"
        return (rectAngle)

    def __repr__(self):
        """internal representation of rectangle"""

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """destructor"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")