#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """ Returns the dictionary description with simple data
    structure for JSOn serialization"""

    return obj.__dict__
