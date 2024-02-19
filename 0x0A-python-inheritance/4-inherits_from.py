#!/usr/bin/python3
"""checks if obj is a subclass but not the exact class"""

def inherits_from(obj, a_class):
    if type(obj) == a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
