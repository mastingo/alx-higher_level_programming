#!/usr/bin/python3
"""importing"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle subclass of Basegeometry"""
    def __init__(self, width, height):
        """init"""
        self.__width = width
        self.__height = height
        if height is True:
            return self.integer_validator('height', height)
        if width is True:
            return self.integer_validator('width', width)
