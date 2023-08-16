#!/usr/bin/python3
def uniq_add(my_list=[]):
    newset = set()
    for i in my_list:
        newset.add(i)
    return sum(newset)
