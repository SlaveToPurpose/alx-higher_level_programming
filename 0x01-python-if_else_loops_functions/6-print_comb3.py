#!/usr/bin/python3
digit = 0
while digit <= 89:
    if digit % 10 == 0:
        digit = digit + 1 + digit // 10
    print("{:02d}".format(digit), end='\n' if digit == 89 else ", ")
    digit = digit + 1
