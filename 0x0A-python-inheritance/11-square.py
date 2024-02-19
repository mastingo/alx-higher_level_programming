#!/usr/bin/python3
"""subclass from class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """init with orivate instance of size"""
        self.__size = size
        self.integer_validator('size', size)

    def area(self):
        """area function"""
        return self.__size ** 2

    def __str__(self):
        """st() output function"""
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
