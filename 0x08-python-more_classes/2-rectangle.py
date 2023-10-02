#!/usr/bin/python3
"""Module containing rectangle class"""


class Rectangle:
    """class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a retangle instance"""

        self.width = width
        self.height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, val):
        """Checks for width attribute"""

        if type(val) != int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, val):
        """Checks ofr height attribute"""

        if type(val) != int:
            raise TypeError("height mst be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """Returns area of rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """returns perimeter of rectangle"""

        return (self.__height*2) + (self.__width*2)
