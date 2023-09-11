#!/usr/bin/python3
"""Module containing Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle classs that inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """initializes width and height values as long as they are +ve"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
