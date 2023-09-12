#!/usr/bin/python3
"""Module containing read_file function"""


def read_file(filename=""):
    """Reads file `filename` and prints it to standard ouput"""
    with open(filename, r, encoding="utf-8") in f:
        for line in f:
            print(line, end="")
