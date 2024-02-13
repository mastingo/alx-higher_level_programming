#!/usr/bin/python3
"""class rectangle"""

class Rectangle:
    """init variable"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must e >= 0')
        self.__height = value

    def area(self):
        """area calc"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter calc"""
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """public instance"""
        string = ''
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(self.height):
            string += '#' * self.width + '\n'
        return string

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'
