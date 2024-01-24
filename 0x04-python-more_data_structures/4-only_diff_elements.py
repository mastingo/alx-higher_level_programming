#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_set = set_1.union(set_2)
    for element in set_1:
        if element in set_2:
            unique_set.remove(element)
    return (unique_set)
