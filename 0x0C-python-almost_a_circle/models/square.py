#!/usr/bin/python3
"""Module containing square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes Square instance"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns width or height property"""

        return self.width

    @size.setter
    def size(self, value):
        """input validator for property"""

        self.variablevalidator("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """overrides str method"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns attributes"""

        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if attributes[i] == "size":
                    self.width = arg
                    self.height = arg
                else:
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                elif hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of instance"""

        return {"id": getattr(self, "id"),
                "x": getattr(self, "x"),
                "size": getattr(self, "width"),
                "y": getattr(self, "y")
                }
