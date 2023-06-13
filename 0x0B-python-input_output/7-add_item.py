#!/usr/bin/python3
"""Adds all arguments topython list and save to file"""


import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        returnList = load_from_json_file("add_item.json")
    except FileNotFoundError:
        returnList = []

    data.extend(sys.argv[1:])

    save_to_json_file(returnList, "add_item.json")
