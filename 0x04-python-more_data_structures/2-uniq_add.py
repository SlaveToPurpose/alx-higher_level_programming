#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_return = 0
    new_list = set(my_list)
    for element in new_list:
        sum_return += element
    return sum_return
