#!/usr/bin/python3
"""subclass"""


class MyList(list):
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
