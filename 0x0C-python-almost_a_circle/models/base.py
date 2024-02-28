#!/usr/bin/python3
"""class called base, base for all my files to come in this """
import json


class Base:
    """private attribute in the class"""
    __nb_object = 0

    def __init__(self, id=None):
        """init method for self and id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """turning json to string"""
        if list_dictionaries is None:
            return '[]'
        elif list_dictionaries == []:
            return '[]'
        else:
            return str(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that takes save to file """
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
            f.write(json_string)
