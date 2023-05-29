#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pop = 0
    if x <= 0:
        print('')
        return pop
    else:
        for element in range(x):
            try:
                print("{:d}".format(my_list[element]), end='')
                pop += 1
            except (ValueError, TypeError):
                pass
    print('')
    return pop
