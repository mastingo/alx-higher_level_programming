#!/usr/bin/python3
"""yeah"""

def read_file(filename=""):
    """more documenting"""
    with open(filename,encoding='utf-8') as f:
        print(f.read(),end='')


