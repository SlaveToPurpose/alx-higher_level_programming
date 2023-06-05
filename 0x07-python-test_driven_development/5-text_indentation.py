#!/usr/bin/python3
"""Definiton for text indentation"""


def text_indentation(text):
    """
    Prints two new line characters after certain charasters
    
    Raise TypeError:
    - if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    output = []

    lines = text.splitlines()

    for i in lines:
        i = i.strip()

    for line in lines:
        if line.endswith(".") or line.endswith("?") or line.endswith(":"):
            output.append(line + '\n\n')
        else:
            output.append(line + '\n')
