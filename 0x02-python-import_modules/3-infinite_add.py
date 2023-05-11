#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    summation = 0
    argument_count = len(argv)
    j = 1
    while argument_count > 1:
        summation = summation + int(argv[j])
        argument_count -= 1
        j += 1

    print("{:d}".format(summation))
