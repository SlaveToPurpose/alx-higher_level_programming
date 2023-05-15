#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        i = 1
        for columns in rows:
            if i < len(rows):
                print("{:d}".format(columns), end=" ")
                i += 1
            else:
                print("{:d}".format(columns), end="")
        print("")
