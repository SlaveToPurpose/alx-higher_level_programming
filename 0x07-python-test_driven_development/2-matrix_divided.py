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
    if len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
        
    for rows in matrix:
        for columns in rows:
            if type(column) is not int or type(column) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(rows) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
        if type(rows) is list:
            pass
        else:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

     if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    