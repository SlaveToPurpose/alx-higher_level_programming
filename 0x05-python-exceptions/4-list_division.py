#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    if list_length <= 0:
        print('')
        return res_list
    else:
        for element in range(list_length):
            try:
                res = my_list_1[element] / my_list_2[element]
            except ZeroDivisionError:
                res = 0
                print("division by 0")
            except (TypeError, ValueError):
                res = 0
                print('wrong type')
            except IndexError:
                res = 0
                print('out of range')
            finally:
                res_list.append(res)
    return res_list
