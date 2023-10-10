#!/usr/bin/python3
"""Module containing write_file function"""


def write_file(filename="", text=""):
    """Writes `text` to file `filename`"""

    with open(filename, 'w', encoding="utf-8") as f:
        x = f.write(text)

    return x
