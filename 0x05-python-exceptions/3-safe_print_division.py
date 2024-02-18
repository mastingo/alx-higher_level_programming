#!/usr/bin/python3

def safe_print_division(a,b):
    if type(a) == int and type(b) == int:
        try:
            c = a / b
            return c
        except:
            c = None
        finally:
            print('Inside result: {}'.format(c))

