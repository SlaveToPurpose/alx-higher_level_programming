#!/usr/bin/python3
"""write obj to text file using json representation"""


import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file"""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
