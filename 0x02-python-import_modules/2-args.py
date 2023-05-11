#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argument_count = len(argv)
    if argument_count == 1:
        print("0 arguments.")
    elif argument_count == 2:
        print("1 argument:")
    elif argument_count > 2:
        print("{:d} arguments:".format(argument_count - 1))

    i = 1
    while argument_count != 1:
        print("{:d}: {:s}".format(i, argv[i]))
        i += 1
        argument_count -= 1
