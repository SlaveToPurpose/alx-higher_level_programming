#!/usr/bin/python3
for digit in range(0, 100):
    end = "\n" if digit == 99 else ", "
    print(F"{digit:02d}", end=end)
