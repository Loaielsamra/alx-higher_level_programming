#!/usr/bin/python3
'''
    This is a module for a square
    '''


class Square:
    '''
        The class square itself
        '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''
            This sets the size attribute
            '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        '''
            sets the position attribute
            '''
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''
            returns current square's area
            '''
        return self.__size * self.__size

    def my_print(self):
        '''
            This prints the square using #
            if size == 0 prints a newline
            '''
        if self.__size == 0:
            print()
            return
        for spaces in range(self.__position[1]):
            print()
        for h in range(self.__size - 1):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
        return "{}{}".format(" " * self.__position[0], "#" * self.__size)

    def __str__(self):
        return self.my_print()
