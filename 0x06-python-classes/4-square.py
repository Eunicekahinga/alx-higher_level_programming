#!/usr/bin/python3
''' A square class that is base on 3-square,py'''


class Square:
    '''Private instance attribute, size which is an int'''

    def __init__(self, size=0):
        '''initialization of private attribute, size which is an int'''
        self.size = size

    def area(self):
        '''Returns current square area'''

        return (self.__size ** 2)

    def size(self):
        '''Retrieves private instance attribute, size'''
        return self.__size

    def size(self, value):
        '''Property setter to set it'''
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
