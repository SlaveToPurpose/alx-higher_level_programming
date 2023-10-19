#!/usr/bin/python3

"""Base class

The goal of it is to manage id attribute in all
your future classes and to avoid duplication.
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation

        Parameters:
        - list_dictionaries(list): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list of instaances to a file

        Parameters:
        - list_objs (list): List of inherited base instances
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, 'w') as f:
                f.write("[]")
        else:
            dict = []
            for obj in list_objs:
                dict.append(obj.to_dictionary())

            jsonString = cls.to_json_string(dict)
            with open(filename, 'w') as f:
                f.write(jsonString)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation

        Parameters:
        - json_string(string): string representing list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
