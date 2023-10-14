#!/usr/bin/python3
"""Moduel containing Base class"""


class Base:
    """Base class itself"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class instance"""

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
