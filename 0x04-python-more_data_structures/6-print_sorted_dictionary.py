#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mydic = list(a_dictionary.keys())
    mydic.sort()
    for i in mydic:
        print("{}: {}".format(i, mydic[i]))
