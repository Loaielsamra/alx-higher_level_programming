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

        self.variablevalidator("width", value)
        self.__width = value

    @property
    def height(self):
        """returns private height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Validates height attribute"""

        self.variablevalidator("height", value)
        self.__height = value

    @property
    def x(self):
        """returns private x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """Validates x attribute"""

        self.variablevalidator("x", value)
        self.__x = value

    @property
    def y(self):
        """returns private y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """Validates y attribute"""

        self.variablevalidator("y", value)
        self.__y = value

    def area(self):
        """Returns area of rectangle instance"""

        return self.__width*self.__height

    def display(self):
        """prints rectangle instance with #"""

        rectangle =""
        for i in range(self.__y):
            rectangle += '\n'
        for i in range(self.__height - 1):
            rectangle += " "*self.__x + "#"*self.__width + '\n'
        rectangle += " "*self.__x + "#"*self.__width
        print(rectangle)

    def __str__(self):
        """Overrides the str method"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                                                     self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
    
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of instance"""

        return {"x": getattr(self, "x"),
                "y": getattr(self, "y"),
                "id": getattr(self, "id"),
                "height": getattr(self, "height"),
                "width": getattr(self, "width")
                }

    @staticmethod
    def variablevalidator(varname, value):
        """Validates variables"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(varname))
        if varname == "width" or varname == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(varname))
        if varname == "x" or varname == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(varname))
