#!/usr/bin/python3
"""Module containing `Rectangle` class"""
Base = __import__('base').Base


class Rectangle(Base):
    """`Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returning property value"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets value of private attribute"""

        self.settervalidation("width", value)
        self.__width = value

    @property
    def height(self,):
        """return property value"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets value of private attribute"""

        self.settervalidation("height", value)
        self.__height = value

    @property
    def x(self):
        """returns property value"""

        return self.__x

    @x.setter
    def x(self, value):
        """sets value of private attribute"""

        self.settervalidation("x", value)
        self.__x = value

    @property
    def y(self):
        """returns property value"""

        return self.__y

    @y.setter
    def y(self, value):
        """sets value of private attribute"""

        self.settervalidation("y", value)
        self.__y = value

    def area(self):
        """returns area of rectangle"""

        return (self.__width * self.__height)

    def display(self):
        """displays rectangle using '#'"""

        displayedrectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            displayedrectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(displayedrectangle, end="")


    @staticmethod
    def settervalidation(attr, value):
        """validates attribuet values"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr))

        if attr == "x" or attr == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attr))
        else:
            if value <= 0:
                raise ValueError("{} must be > 0".format(attr))

    def __str__(self):
        """overrides str"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                self.width, self.height)
