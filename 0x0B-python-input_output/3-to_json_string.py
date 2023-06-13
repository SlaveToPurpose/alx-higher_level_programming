#!/usr/bin/python3
"""Returns JSON representation of an object"""


import json


def to_json_string(my_obj):
    """return json representation"""
    a = json.dumps(my_obj)
    return a
