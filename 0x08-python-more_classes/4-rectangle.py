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
        """returns private width attribute"""

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
        """returns height attribute"""

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

        if (self.__width == 0 or self.__height == 0):
            peri = 0
        else:
            peri = (self.__width*2) + (self.__height*2)
        return peri

    def __str__(self):
        """returns sting representation of object"""

        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle

        for i in range(self.height - 1):
            rectangle += "#"*self.__width + "\n"
        rectangle += "#"*self.__width

        return rectangle

    def __repr__(self):
        """Returns official string representation"""

        rectangle = "{}({},{})".format(self.__class__.__name__,
                                       self.__width, self.__height)
        return rectangle
