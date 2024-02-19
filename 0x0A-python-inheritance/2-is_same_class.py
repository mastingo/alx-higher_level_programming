#!/usr/bin/python3
"""def is_same_class(obj, a_class):
    return isinstance (obj, a_class)"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return (type(obj) is a_class)
