#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [my_list[i - 1] for i in range(1, len(my_list) + 1)]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
    return my_list
