#!/usr/bin/python3
"""importing"""


import importlib

module = importlib.import_module("7-base_geometry")

BaseGeometry = module.BaseGeometry
"""class rectangle inheriting from basegeom)"""


class Rectangle(BaseGeometry):
    """init private instances"""
    def __init__(self, width, height):
        """init"""
        self.__width = width
        self.__height = height
        super().__init__()
        if height is True:
            return self.integer_validator('height', height)
        if width is True:
            return self.integer_validator('width', width)
