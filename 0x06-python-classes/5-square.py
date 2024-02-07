#!/usr/bin/python3
'''A square class based on 2-square.py'''


class Square:
    '''A private attribute int size'''

    def __init__(self, size=0):
        '''Optional initialization of size, int'''
        self.size = size

    def area(self):
        '''Returns current square area'''
        return (self.__size ** 2)

    @property
    def size(self):
        '''Retrieves private instance attribute, size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Property setter to set it'''
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self. __size)
