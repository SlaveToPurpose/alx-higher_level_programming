#!/usr/bin/python3
"""Definition for matrix division"""


def matrix_divided(matrix, div):
    """Returns new matrix with divided functions
    
    Raise TypeError
    - if rows of matrix are not the same size
    - if div is not an integer or float
    - if the matrix is not a list of ints or floats
    Raise ZeroDivisionError
    - if div = 0
    """
    if div is int or div is float:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
        