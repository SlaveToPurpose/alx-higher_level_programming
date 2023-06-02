#!/usr/bin/python3
"""Definiton for Say My Name"""


def say_my_name(first_name, last_name=""):
    """
        Function prints first and last names
        Raise TypeError
            - if first name is not a string
            - if last name is not a string
    """
    if type(first_name) is str:
        pass
    else:
        raise TypeError("first_name must be a string")

    if type(last_name) is str:
        pass
    else:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))