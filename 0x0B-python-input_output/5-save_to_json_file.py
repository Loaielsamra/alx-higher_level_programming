#!/usr/bin/python3
"""Module containing save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """saves `my_obj` to file `filename` in JSON representation"""

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
