#!/usr/bin/python3
"""Module containing load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an object from a Json file"""

    with open(filename, 'r', encoding="utf-8") as f:
        obj = json.load(f)

    return obj
