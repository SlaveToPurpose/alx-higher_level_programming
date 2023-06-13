#!/usr/bin/python3
"""return an object representated by a JSON string"""


import json


def from_json_string(my_str):
    """from json to object"""

    a = json.loads(my_str)
    return a
