#!/usr/bin/python3
"""module containing to_json_string function"""


def to_json_string(my_obj):
    """returns JSON representation of an object(string)"""

    return json.dump(my_obj)
