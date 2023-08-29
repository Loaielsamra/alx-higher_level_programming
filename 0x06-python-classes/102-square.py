#!/usr/bin/python3
'''
    This is a module for a square
    '''


class Square:
    '''
        The class square itself
        '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
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
    
    def __le__(self, other):
        '''
            less than or equal <=
            '''
        return(self.area() <= other.area())
    def __lt__(self, other):
        '''
            less than <
            '''
        return(self.area() < other.area())
    def __gt__(self, other):
        '''
            greater than >
            '''
        return(self.area() > other.area())
    def __gl__(self, other):
        '''
            greater than or equal
            '''
        return(slef.area() >= other.rea())
    def __eq__(self, other):
        '''
            equal to ==
            '''
        return(self.area() == other.area())
    def __ne__(self, other):
        '''
            not equal to !=
            '''
        return(self.area() != other.area())
