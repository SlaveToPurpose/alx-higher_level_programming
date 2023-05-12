#!/usr/bin/python3
def no_c(my_string):
    resultant = ""
    for element in my_string:
        if element == 'c' or element == 'C':
            continue
        else:
            resultant = resultant + element
    return resultant
