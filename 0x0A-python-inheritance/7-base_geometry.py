#!/usr/bin/python3
"""class"""

class BaseGeometry:
    """public method"""

    def area(self):
        """raise"""
        raise Exception ('area() is not implemented')

    """public method"""
    def integer_validator(self, name, value):
        """if statement"""
        if type(value) != int:
            """raise"""
            raise TypeError('{:s} must be an integer'.format(name))
        """else"""
        elif value <= 0:
            """raise"""
            raise ValueError('{:s} must be greater than 0'.format(name))
