#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return_set = set()
    return_set = set_1 ^ set_2
    return return_set
