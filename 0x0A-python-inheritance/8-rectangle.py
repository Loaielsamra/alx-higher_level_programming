#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle classs that inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """initializes width and height values as long as they are +ve"""
        self.integervalidator("width", width)
        self.integervalidator("height", height)
        self.__width = width
        self.__height = height
