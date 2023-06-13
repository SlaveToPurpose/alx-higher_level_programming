#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, aClass):
    """returns true if @obj is not an instance of aClass"""
    return (type(obj) is aClass)
