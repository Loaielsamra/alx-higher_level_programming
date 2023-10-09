#!/usr/bin/python3
"""Module containing MyList Class"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        cp = list.copy(self)
        list.sort(cp)
        print(cp)
