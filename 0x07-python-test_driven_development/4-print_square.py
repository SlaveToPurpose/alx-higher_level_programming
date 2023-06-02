#!/usr/bin/python3
"Definition to print a square with an #"


def print_square(size):
    """Prints a square of size 'size' 
    
    Raises TypeError
        - if size is not an integer
        - if size is a float 
        - if size is less than 0
    Raises ValueError
        - if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)
    for i in range(size):
        print('#' * size)