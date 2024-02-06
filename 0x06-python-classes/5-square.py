#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return (self.__size ** 2)

    def size(self):
        return self.__size

    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size = 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self. __size)
