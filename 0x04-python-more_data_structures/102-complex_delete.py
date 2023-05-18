#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dic_copy = a_dictionary.copy()
    for key, val in dic_copy.items():
        if val != value:
            continue
        else:
            a_dictionary.pop(key)
    return a_dictionary
