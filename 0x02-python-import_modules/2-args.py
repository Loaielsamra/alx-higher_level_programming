#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg = "arguments"
    length = len(argv) - 1
    punc = "."
    if (length == 1):
        arg = "argument"
    if (length - 1 >= 0):
        punc = ":"

    print("{} {}{}".format(length, arg, punc))

    for index, arg in enumerate(argv):
        if (index > 0):
            print("{}: {}".format(index, arg))
