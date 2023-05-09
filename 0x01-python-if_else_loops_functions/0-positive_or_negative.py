#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print(F"{number:d} is negative")
elif number > 0:
    print(F"{number:d} is positive")
elif number == 0:
    print(F"{number:d} is zero")
