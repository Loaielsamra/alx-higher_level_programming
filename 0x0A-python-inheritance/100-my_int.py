#!/usr/bin/python3
"""Module containing MyInt class"""


class MyInt(int):
    """MyInt class that inherits from int
    and has == and != operators switched"""

    def __init__(self, value):
        """Initializes MyInt instance"""

        self.value = value

    def __eq__(self, otherval):
        """ actualy != operator"""

        return (self.value != otherval)

    def __ne__(self, otherval):
        """actually == operator"""

        return (self.value == otherval)
