#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module containing the rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Initializes a new rectangle instance"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle"""

        return (self.__width*self.__height)

    def __str__(self):
        """prints representation of rectangle"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
