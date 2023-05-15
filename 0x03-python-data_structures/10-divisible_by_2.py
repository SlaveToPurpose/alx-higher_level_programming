#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    boolean_list = my_list[:]
    for element in my_list:
        if element % 2 == 0:
            boolean_list[i] = True
        else:
            boolean_list[i] = False
        i += 1
    return boolean_list
