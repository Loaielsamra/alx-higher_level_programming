#!/usr/bin/python3
"""Module containing is_same_class function"""


def is_same_class(obj, a_class):
    """returns True if obj is exactly an instance of `a_class`
        otherwise returns False"""

    if type(obj) != a_class:
        return False

    return True
