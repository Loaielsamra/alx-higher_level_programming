#!/usr/bin/python3
'''
    This is a module for a square
    '''


class Square:
    '''
        The class square itself
        '''
    def __init__(self, size=0):
        '''
            This sets the size attribute
            '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
            returns current square's area
            '''
        return self.__size * self.__size
