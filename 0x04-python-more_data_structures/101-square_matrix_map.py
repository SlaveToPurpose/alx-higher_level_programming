#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [col**2 for col in row], matrix))
