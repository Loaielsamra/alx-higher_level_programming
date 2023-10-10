#!/usr/bin/python3
"""Module containing add_item function"""
import sys
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file


def add_item(args, filename):
    """adds all arguments to a Python list, and then save them to a file"""

    try:
        toadd = load_from_json(filename)
    except Exception:
        toadd = []

    for item in args:
        toadd.append(item)

    save_to_json(toadd, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
