#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module containing the rectangle class"""


class Rectangle(BaseGeometyr):
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Initializes a new rectangle instance"""

        BaseGeometry.integer_validator("width", width)
        BaseGeometry.integer_validator("height", height)
        self.__width = width
        self.__height = height
