#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class child of base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for rectangle
        Parameters:
        widht(int): width of rect
        height(int): height of rectangle
        x(int): x coordinate of rectangle
        y(int): y coordinate of rectangle
        id(int): ID of rectangle

        Returns:
        None
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area value of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Print Rectangle to stdout using #

        Returns:
        None
        """
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return string representation of Rectangle

        Returns:
        str: string representation
        """
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance
        by assigning an argument to each attribute.

        Parameters:
        - args (int): Arguments.

        Returns:
        None
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of Rectangle

        Returns:
        dict: Dictionary
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
