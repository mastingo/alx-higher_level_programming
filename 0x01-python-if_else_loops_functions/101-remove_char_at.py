#!/usr/bin/python3

'''definition for poping charachters'''


def remove_char_at(str, n):
    new_string = ''
    for index, char in enumerate(str):
        if index != n:
            new_string += char
    return new_string
