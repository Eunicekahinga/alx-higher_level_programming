#!/usr/bin/python3
"""A square class defined as in 1-square.py"""


class Square:
    """Size is a private instance attribute and is an int"""

    def __init__ (self, size=0):
        """Instantiation with optional size which is an int"""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
