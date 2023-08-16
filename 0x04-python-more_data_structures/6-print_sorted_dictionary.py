#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mydic = []
    if a_dictionary:
        for keys, items in a_dictionary.items():
            mydic.append(keys)

    mydic.sort()
    for i in mydic:
        print("{}: {}".format(i, mydic[i]))
