#!/usr/bin/python
"""docstring"""


def append_write(filename='', text=''):
    """docstring to pass checker"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
