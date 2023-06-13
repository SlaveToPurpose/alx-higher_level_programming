#!/usr/bin/python3
"""Appending string to a file"""


def append_write(filename="", text=""):
    """append string at the end of a text file, and
    return the number of characters"""

    with open(filename, "a", encoding="utf-8") as f:
        char_count = f.write(text)
    return char_count
