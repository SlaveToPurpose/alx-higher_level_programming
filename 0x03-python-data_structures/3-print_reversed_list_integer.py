#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    indx = len(my_list) - 1
    while indx >= 0:
        print("{:d}".format(my_list[indx]))
        indx -= 1
