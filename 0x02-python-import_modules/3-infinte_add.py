#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0

    for i, num in enumerate(argv):
        if (i > 0):
            sum += int(num)

    print("{:d}".format(sum))
