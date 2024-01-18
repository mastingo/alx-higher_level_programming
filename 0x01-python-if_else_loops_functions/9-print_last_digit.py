#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, int):
        number = str(number)
        print('{}'.format(number[-1]), end='')
        return number[-1]
