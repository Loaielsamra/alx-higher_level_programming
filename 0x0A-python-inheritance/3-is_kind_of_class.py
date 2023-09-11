#!/usr/bin/python3
""" Module for the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """returns True if obj is an instance of,
    or an instnace of a child class of a_class"""

    if type(obj) == a_class:
        return True
    elif issubclass(type(obj), a_class):
        return True

    return False
