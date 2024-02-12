#!/usr/bin/python3
'''A class rectangle, defining a rectangle based on 0-rectangle.py'''

class Rectangle:
    '''A class defining a rectangle'''
    def __init__(self, width=0, height=0):
        '''The class rectangle initialized with 'height' and 'width'.

        Args:
            height (int): rectangle height. value is >= 0
            width (int): rectangle width. value is >= 0
        '''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter function for 'width' attribute.

        Returns: 'width' value attribute.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter function for the 'width' attribute.

        Args:
            value(int): value to be used for 'width'

        Raises:
            TypeError: if not int, with the message width must be an integer
            ValueError: if value is less than 0 with the message width must be >= 0
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Getter function for 'height' attribute.

        Returns: 'height' value attribute.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter function for the 'height' attribute.

        Args:
            value(int): value to be used for 'height'

        Raises:
            TypeError: if not int, with the message height must be an integer
            ValueError: if value is less than 0 with the message height must be >= 0
        '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value< 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
