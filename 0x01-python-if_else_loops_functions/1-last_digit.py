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
part1 = "Last digit of {} is {}".format(number, r_num)
if r_num == 0:
    part2 = "and is 0"
elif r_num > 5:
    part2 = "and is greater than 5"
elif r_num < 6:
    part2 = "and is less than 6 and not 0"
print(part1 + " " + part2)
