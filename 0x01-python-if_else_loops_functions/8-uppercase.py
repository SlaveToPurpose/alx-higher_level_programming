#!/usr/bin/python3
def uppercase(string):
    string_1 = ""
    for i in string:
        if ord(i) > 96 and ord(i) < 123:
            string_1 += "{:c}".format(ord(i) - 32)
        else:
            string_1 += i

    print(string_1)
