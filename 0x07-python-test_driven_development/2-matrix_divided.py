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
    if type(div) is int or type(div) is float:
        pass
    else:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
        
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                
    divided_matrix = []
    for row in matrix:
        divided_row = []
        for element in row:
            divided_row.append(round(element / div, 2))
        divided_matrix.append(divided_row)

    return divided_matrix
