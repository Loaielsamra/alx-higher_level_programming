#!/usr/bin/python3
'''
    Module for function lookup()
    '''


def lookup(obj):
    '''
        returns a list of all available attributes and methods for `obj`
        '''
    return list(dir(obj))
