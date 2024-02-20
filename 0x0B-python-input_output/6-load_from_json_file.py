#!/usr/bin/python3
"""mixed"""


import json


def load_from_json_file(filename):
    """docstring"""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
