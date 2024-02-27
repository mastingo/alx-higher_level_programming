#!/usr/bin/python3
"""class called base, base for all my files to come in this """


class Base:
    """private attribute in the class"""
    __nb_object = 0

    def __init__(self, id=None):
        """def"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    def to_json_string(list_dictionaries):
        """turning json to string"""
        if list_dictionaries is None:
            return '[]'
        else:
            return str(list_dictionaries)