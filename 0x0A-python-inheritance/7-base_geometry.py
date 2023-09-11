#!/usr/bin/python3
"""Module containing BaseGeometry class"""


class BaseGeometry:
    """The class itself"""
    def __init__(self):
        pass

    def area(self):
        """ Raises an Exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates if value is an integer and is greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
