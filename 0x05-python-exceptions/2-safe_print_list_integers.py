#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for element in my_list:
        if n == x:
            break
        try:
            print('{:d}'.format(element, end=''))
            n += 1
        except (ValueError, TypeError):
            continue
