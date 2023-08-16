#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        mylist = list(a_dictionary.keys())

        for i in mylist:
            a_dictionary[i] *= 2
        return a_dictionary
