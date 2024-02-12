#!/usr/bin/python3
'''A class rectangle that defines a rectangle based on 2-rectangle.py'''


class Rectangle:
    '''A class rectangle, to create a rectangle'''
    def __init__(self, width=0, height=0):
        '''The class rectangle initialized with 'height' and 'weight'.

        Args:
            height (int): height of a rectangle, value >= 0.
            width (int): width of a rectangle, value >= 0.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter function for the attribute 'width'

        Returns: value of the attribute 'width'
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter function for the attribute 'width'

        Args:
            value (int): value for 'width' attribute

        Raises:
            TypeError: if value is not type (int)
            ValueError: if value is < 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''getter function for the attribute 'height'

        Returns: value of the attribute 'height'
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter function for the attribute 'height'

        Args:
            value (int): value for 'height' attribute

        Raises:
            TypeError: if value is not type (int)
            ValueError: if value is < 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''A way to calculate the area of Rectangle instance'''
        return self.width * self.height

    def perimeter(self):
        '''A way to compute the perimeter of Rectangle instance.

        Returns: 2* (w + h) else 0 if w and h are equal to 0
        '''
        return 2*(self.width + self.height) * bool(self.width and self.height)

    def __str__(self):
        '''Prints the rectangle with the character #.

        Return: If width and height = 0 return empty string else #
        '''
        rec = ""
        if not (self.width and self.height):
            return rec
        for i in range(self.height):
            rec += '#'*self.width + '\n'
        return rec[:-1]

    def __repr__(self):
        '''Prints string representation of rectangle
        Should be able to create new instance using eval()
        '''

        return "Rectangle({}, {})".format(self.width, self.height)
