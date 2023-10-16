#!/usr/bin/python3

"""Base class"""

import json
import csv
import turtle


""" “base” of all other classes.
The goal of it is to manage id attribute in all
your future classes and to avoid duplication
"""

class Base:
    """Base class for managing ids"""


    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Parameters:
        - id (int)
        Returns:
        None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
