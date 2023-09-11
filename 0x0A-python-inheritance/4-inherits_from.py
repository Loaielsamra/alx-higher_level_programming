#!/usr/bin/python3
"""Module containing inherits_from function"""


def inherits_from(obj, a_class):
    """
        returns True if `obj` is an instance of a class derived from a_class
        """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
