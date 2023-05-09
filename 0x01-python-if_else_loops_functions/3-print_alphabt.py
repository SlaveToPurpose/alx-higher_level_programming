#!/usr/bin/python3
a = 97
printable = ""
while a < 123:
    if a == 113 or a == 101:
        a = a + 1
        continue
    print("{:c}".format(a), end="")
    a = a + 1
