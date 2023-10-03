#!/usr/bin/python3
"""Module containing print_square function"""


def print_square(size):
    """prints square using '#' with `size` height and width"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#"*size)
