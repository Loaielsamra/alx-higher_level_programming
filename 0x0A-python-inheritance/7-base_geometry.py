#!/usr/bin/python3
"""Module containing the BaseGeometry class"""


class BaseGeometry:
    """Class BaseGeometry itself"""

    def area(self):
        """Raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if `name`'s value is an integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
