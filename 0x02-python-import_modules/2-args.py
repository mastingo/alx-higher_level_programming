#!/usr/bin/python3
import sys


if __name__ == "__main__":
    length = len(sys.argv) - 1
    argument = ' '.join(sys.argv[1:])
    if length == 1:
        print("{} argument:".format(length))
        print("{}. {}".format(length, argument))
    elif length == 0:
        print("0 arguments")
    else:
        print('{} arguments:'.format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]))
