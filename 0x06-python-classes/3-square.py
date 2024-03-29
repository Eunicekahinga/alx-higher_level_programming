#!/usr/bin/python3
'''A square class based on 2-square.py'''


class Square:
    '''A private attribute int size'''

    def __init__(self, size=0):
        '''Optional initialization of size, int'''

        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
