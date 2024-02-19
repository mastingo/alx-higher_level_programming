#!/usr/bin/python3
"""importing class"""


BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        """init private instances"""
        self.__width = width
        self.__height = height

    def area(self):
        """defines func"""
        return self.__width * self.__height

    def __str__(self):
        """defines string funct"""
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
