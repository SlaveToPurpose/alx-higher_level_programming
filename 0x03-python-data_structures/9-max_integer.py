#!/usr/bin/python3
def max_integer(my_list=[]):
    if (not my_list):
        return None
    val = 0
    return_val = my_list[0]
    for element in my_list:
        val = element
        if return_val < val:
            return_val = val
        else:
            continue
    return return_val
