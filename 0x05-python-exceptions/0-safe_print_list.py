#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_count = 0

    if x <= 0:
        pass
    else:
        for element in my_list:
            try:
                print("{}".format(element), end='')
                list_count += 1
                if list_count == x:
                    print('')
                    return list_count
            except Exception:
                break
        print("")
    return list_count
