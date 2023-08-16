#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mydic = []

    for keys, values in a_dictionary.items():
        mydic.append(keys)

    mydic.sort()
    for i in mydic:
        print("{}: {}".format(mydic, mydic[i]))
