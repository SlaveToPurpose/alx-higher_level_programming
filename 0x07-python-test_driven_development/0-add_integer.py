#!/usr/bin/python3
"""Defition for integer addition"""


def add_integer(a, b=98):
    """Returns addition of a and b
    
    Raise:
        TypeError if a or b is not an integer or float
    """
    if type(a) is int or type(a) is float:
        pass
    else:
        raise TypeError("a must be an integer")

    if type(b) is int or type(b) is float:
        pass
    else:
        raise TypeError("b must be an integer")
        
    return int(a) + int(b)