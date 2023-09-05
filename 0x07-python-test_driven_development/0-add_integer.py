#!/usr/bin/python3
'''
    Adds to integers
    '''
def add_integer(a, b=89):
    '''
        Adds 2 integers
        '''
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
