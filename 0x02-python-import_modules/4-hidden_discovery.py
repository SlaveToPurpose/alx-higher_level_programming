#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for argument in dir(hidden_4):
        if argument[0] == '_' and argument[1] == '_':
            continue
        else:
            print("{:s}".format(argument))
