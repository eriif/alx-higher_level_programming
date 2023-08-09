#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = abs(number) % 10
if number < 0:
    i = -i
print("Last digit of {} is {} and is ".format(number, i), end="")
if i > 5:
    print("greater than 5")
elif i == 0:
    print("0")
else:
    print("less than 6 and not 0")
