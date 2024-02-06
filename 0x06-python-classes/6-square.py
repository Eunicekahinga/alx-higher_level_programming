#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    def position(self):
        return self.__position

    def position(self, position):
        if isinstance(position, tuple):
            if len(position) == 2:
                if isinstance(position[0], int) and isinstance(position[1], int):
                    if position[0] >= 0 and position[1] >= 0:
                        self.__position = position
                        return
        
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

