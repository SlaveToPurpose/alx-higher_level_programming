#!/usr/bin/python3
"""Sqaure class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square

        Parameters:
        - size (int): Size of the square
        - x (int): X-coordinate of the square
        - y (int): Y-coordinate of the square
        - id (int): ID of the square

        Raises:
        - TypeError: If size, x, y, or id is not an integer.
        - ValueError: If size, x, or y is < 0.

        Returns:
        None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of Square

        Returns:
        str: String
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size.

        Parameters:
        - value (int): Value to set for size

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is <= 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square with the provided arguments.

        Parameters:
        - args (int): Arguments
        - kwargs (dict): Key-value pairs

        Returns:
        None
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.y = args[2]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of Square

        Returns:
        dict: Dictionary
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
