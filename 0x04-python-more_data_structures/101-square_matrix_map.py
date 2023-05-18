#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda col: col**2, row)) for row in matrix]
