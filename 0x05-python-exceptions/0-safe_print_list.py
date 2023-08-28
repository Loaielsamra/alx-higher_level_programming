#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i, j in enumerate(my_list):
            if (i < x):
                print(j, end="")
                counter += 1
    except IndexError:
        pass
    print()
    return counter
