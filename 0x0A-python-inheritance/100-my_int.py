#!/usr/bin/python3
"""Module containing MyInt class"""


class MyInt(int):
    """class itself"""

    def __ne__(self, other):
        """switch != with =="""
        return self.real == other

    def __eq__(self, other):
        """sqitches == with != """
        return self.real != other
