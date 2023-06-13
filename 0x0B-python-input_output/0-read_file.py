#!/usr/bin/python3
"""a function that reads a text file"""


def read_file(filename=""):
    """Reads a text file and prints out to stdout"""

    with open(filename, encoding="utf-8") as f:
        for i in f.readlines():
            print(i.rstrip())

