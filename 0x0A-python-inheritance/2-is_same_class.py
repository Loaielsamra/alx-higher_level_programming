#!/usr/bin/python3
"""Module for is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if `obj` is exactly an instance of a_class"""
    if type(obj) == a_class:
        return True
    return False
