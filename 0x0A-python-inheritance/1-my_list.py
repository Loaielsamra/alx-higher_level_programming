#!/usr/bin/python3
'''
    Module for class `MyList`
    '''


class MyList(list):
    '''
        Class MyList itself
        '''
    def __init__(self):
        '''
            initializes the object
            '''
        super().__init__()

    def print_sorted(self):
        '''
            prints ascendingly sorted list
            '''

        print(sorted(self))
