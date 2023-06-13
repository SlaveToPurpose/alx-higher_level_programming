#!/usr/bin/python3
"""Tests if an object inherits from a class"""


def inherits_from(obj, a_class):
    """True if @obj is an instance of a class that inherited
    from @a_class"""
    pi = issubclass(type(obj), a_class) and (type(obj) is not a_class)
    return pi