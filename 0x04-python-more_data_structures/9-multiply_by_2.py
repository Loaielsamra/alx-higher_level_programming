#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = {}

    for key, value in a_dictionary.items():
        newdic.update({key: (value * 2)})

    return newdic
