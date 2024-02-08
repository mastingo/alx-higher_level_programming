#!/usr/bin/python3
"""Square class"""


class Square:
    """defines square attributes"""
    def __init__(self, size):
        """sets size as instance"""
        self.__size = size

    @property
    def size(self):
        """getter of the size instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance (value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """yessir"""
        return self.__size ** 2

    def my_print(self):
        """yessir"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
             print("".join(["#" for j in range(self.__size)]))

