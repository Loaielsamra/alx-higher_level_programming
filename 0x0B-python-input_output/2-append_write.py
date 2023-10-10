#!/usr/bin/python3
"""Module containing append_write"""


def append_write(filename="", text=""):
    """appends `text` to file `filename`"""

    with open(filename, 'a', encoding="utf-8") as f:
        x = f.write(text)

    return x
