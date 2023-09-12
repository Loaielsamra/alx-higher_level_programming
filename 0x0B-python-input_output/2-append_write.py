#!/usr/bin/python3
"""Module containing append_write function"""


def append_write(filename="", text=""):
    """Appends `text` to file `filename`"""
    with open(filename, 'a', encoding="utf-8"):
        return f.write(text)
