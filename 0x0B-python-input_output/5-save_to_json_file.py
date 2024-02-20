#!/usr/bin/python3
"""json"""


import json


def save_to_json_file(my_obj, filename):
    """fucntion"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
