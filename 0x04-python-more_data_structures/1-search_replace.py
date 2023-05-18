#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return_list = []
    if my_list:
        for element in my_list:
            if element != search:
                return_list.append(element)
            else:
                return_list.append(replace)
        return return_list
    else:
        return my_list
