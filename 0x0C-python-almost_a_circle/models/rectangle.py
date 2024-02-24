#!/usr/bin/python3
from models.base import Base

"""rectangle class inheriting from base"""


class Rectangle(Base):
    """initialising rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """super method to access id"""
        super().__init__(id)

    @property
    def width(self):
        """property setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter makes sure var is an int"""
        if width is not int:
            raise TypeError('value needs to be an integer')
        else:
            self__width = value

    @property
    def height(self):
        """property getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """make sure height is an int"""
        if height is not int:
            raise TypeError('value must be an integer')
        else:
            self.__height = value

    @property
    def x(self):
        """property getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter"""
        if x is not int:
            raise TypeError('value must be an int')
        else:
            self.__x = value

    @property
    def y(self):
        """property getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter"""
        if y is not int:
            raise TypeError('Value is  must be an int')
        else:
            self.__y = value
