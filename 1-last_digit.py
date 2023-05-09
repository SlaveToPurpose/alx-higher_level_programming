#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
r_num = number
while True:
    if r_num > 0:
        r_num = r_num % 10
    else:
        r_num = ((r_num * -1) % 10) * -1
    if r_num > 10 or r_num < -10:
        continue
    else:
        break
print(F"Last digit of {number:d} is {r_num:d}")
r_num = number
