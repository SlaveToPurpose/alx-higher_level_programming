#!/usr/bin/python3
"""Adds all arguments topython list and save to file"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    returnList = load_from_json_file("add_item.json")
except FileNotFoundError:
    returnList = []

if (len(sys.argv)) > 1:
    for arg in range(1, len(sys.argv)):
        returnList.append(sys.argv[arg])

save_to_json_file(returnList, "add_item.json")
