#!/usr/bin/python3
"""checks if obj is a subclass but not the exact class"""


def inherits_from(obj, a_class):
    """funvtional"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
