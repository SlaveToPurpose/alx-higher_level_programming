#!/usr/bin/python3
"""search & update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text after each line containing a specific string
    """

    data = ""

    with open(filename, encoding="utf-8") as file:
        for line in file:
            data.append(line)
            if search_string in line:
                data += new_string

    with open(filename, "w", encoding="utf-8") as file2:
        file2.write(data)
