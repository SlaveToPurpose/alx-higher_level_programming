#!/usr/bin/python3
def fizzbuzz():
    for digit in range(1, 101):
        if digit % 15 == 0:
            print("FizzBuzz", end=" ")
        elif digit % 5 == 0:
            print("Buzz", end=" ")
        elif digit % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(F"{digit:d}", end=" " if digit < 100 else "")
