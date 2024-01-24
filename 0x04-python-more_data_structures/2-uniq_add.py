#!/usr/bin/python3
def uniq_add(my_list=[]):
    sort_list = sorted(my_list)
    new_list = set(sort_list)
    result = sum(new_list)
    return result
