#!/usr/bin/python3
def no_c(my_string):
    strnew = ""
    for i in my_string:
        if (i != 'c' or i != 'C'):
            strnew += i
    return (strnew)
