#!/usr/bin/python3
"""Python class like from the previous question"""


class Square:
    """creating an initing a class"""
    def __init__(self, size=0):
        """ initializes args """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """method that find area of a square"""
        return self.__size ** 2

