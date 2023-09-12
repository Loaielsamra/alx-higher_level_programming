#!/usr/bin/python3
"""Module containing load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an object from JSON file"""
    with open(filename, encoding="utf-8") as f:
        x = json.load(f)
    return x
