#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) == 4:
        arg1 = int(argv[1])
        arg3 = int(argv[3])
        if argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(arg1, arg3, add(arg1, arg3)))
        elif argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(arg1, arg3, sub(arg1, arg3)))
        elif argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(arg1, arg3, mul(arg1, arg3)))
        elif argv[2] == '/':
            print("{:d} / {:d} = {:d}".format(arg1, arg3, div(arg1, arg3)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
