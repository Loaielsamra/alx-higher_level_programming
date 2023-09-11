#!/usr/bin/python3
"""Module contatining Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The `Square class itself"""

    def __init__(self, size):
        """initializes `size` only if greater than 0"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns string representation of square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
