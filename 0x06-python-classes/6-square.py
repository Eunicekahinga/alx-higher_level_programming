#!/usr/bin/python3
''' A square class that is based on 3-square.py'''


class Square:
    '''Private instance attribute, size which is an int'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialization of private attribute, size and position'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''Retrieves private instance attribute, position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Property setter to set position'''
        if isinstance(value, tuple) and len(value) == 2 \
                and isinstance(value[0], int) and isinstance(value[1], int) \
                and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        '''Prints the square with position'''
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
