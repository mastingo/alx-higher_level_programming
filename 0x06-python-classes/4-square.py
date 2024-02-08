#!/usr/bin/python3
"""this is a class of square"""


class Square:
    """innit for this"""
    def __init__(self, size=0):
        self.__size = size
    """property setter"""
    @property
    def size(self):
        return self.__size
    """property getter"""
    @size.setter
    def size(self, value):
        """ arg for value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return value for area"""
        return self.__size ** 2
