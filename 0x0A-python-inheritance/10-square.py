#!/usr/bin/python3
"""subclass with class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """initializing intances"""
        self.__size = size
        self.integer_validator('size', size)

    def area(self):
        """calling area"""
        return self.__size ** 2

    def __str__(self):
        """calling str"""
        return '[Rectangle] {:d}/{:d}'.format(self.__size, self.__size)
