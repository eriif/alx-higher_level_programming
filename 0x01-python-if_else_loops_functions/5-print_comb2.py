#!/usr/bin/python3
for number in range(0, inf):
    if number == inf:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
