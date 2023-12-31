#!/usr/bin/python3
"""Module containg the add_integer function"""


def add_integer(a, b=98):
    """returns the value of the sum between a and b"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a+b)
