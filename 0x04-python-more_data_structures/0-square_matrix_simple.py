#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_matrix.append([y*y for y in row])

    return squared_matrix
