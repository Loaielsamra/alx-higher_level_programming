#!/usr/bin/python3
"""Module containing Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes instance of Square class"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates area of square instance"""

        return (self.__size ** 2)