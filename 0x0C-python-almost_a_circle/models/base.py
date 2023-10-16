#!/usr/bin/python3

"""Base class

The goal of it is to manage id attribute in all
your future classes and to avoid duplication.
"""


class Base:
    """Base class for managing ids.

    Private Class Attributes:
    __nb_object (int): Number of instaniated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Parameters:
        - id (int): id of new Base

        Returns:
        None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
