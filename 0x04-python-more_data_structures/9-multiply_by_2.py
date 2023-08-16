#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dictionary = {}

        for keys, items in a_dictionary.items():
            new_dictionary.update({keys: (items * 2)})

        return new_dictionary
