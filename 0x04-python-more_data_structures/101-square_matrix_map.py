#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda col: col*col, row)) for row in matrix]
