#!/usr/bin/python3
"""write a string to file and return number of chars"""


def write_file(filename="", text=""):
    """write to file"""

    with open(filename, "w") as f:
        num_of_chars = f.write(text)
    return num_of_chars
