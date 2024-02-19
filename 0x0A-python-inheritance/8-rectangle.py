#!/usr/bin/python3
"""importing"""


import importlib
module = importlib.import_module("7-base_geometry")
BaseGeometry = module.BaseGeometry


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
