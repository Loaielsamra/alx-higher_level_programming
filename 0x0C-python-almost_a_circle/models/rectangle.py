#!/usr/bin/python3
"""Module containing Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class instance"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns private width attribue"""

        return self.__width

    @width.setter
    def width(self, value):
        """Validates width attribute"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns private height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Validates height attribute"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns private x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """Validates x attribute"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns private y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """Validates y attribute"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle instance"""

        return self.__width*self.__height

    def display(self):
        """prints rectangle instance with #"""

        rectangle =""
        for i in range(self.__y - 1):
            rectangle += '\n'
        for i in range(self.__height - 1):
            rectangle += " "*self.__x + "#"*self.__width + '\n'
        rectangle += " "*self.__x + "#"*self.__width
        print(rectangle)

    def __str__(self):
        """Overrides the str method"""

        return "Rectangle ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                                                     self.__width, self.__height)
