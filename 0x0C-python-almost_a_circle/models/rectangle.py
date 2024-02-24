#!/usr/bin/python3
from models.base import Base

"""rectangle class inheriting from base"""


class Rectangle(Base):
    """initialising rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """super method to access id"""
        super().__init__(id)

    @property
    def width(self):
        """property setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter makes sure var is an int"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """property getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """make sure height is an int"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """property getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """property getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """method to do area fo the rectangle"""
        return self.__width * self.__height
