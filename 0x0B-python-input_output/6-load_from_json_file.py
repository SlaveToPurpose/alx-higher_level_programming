#!/usr/bin/python3
"""Create an object from a json file"""


import json


def load_from_json_file(filename):
    """create obj from json file"""

    with open(filename, "r", encoding="utf-8") as f:
        json_obj = json.load(f)
    return json_obj
