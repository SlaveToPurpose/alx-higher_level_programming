#!/usr/bin/python3
def print_last_digit(number):
    while True:
        if number > 0:
            number = number % 10
        else:
            number = ((number * -1) % 10)
        if number > 10 or number < -10:
            continue
        else:
            break

    print(number, end="")
    return number
