#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argument = (sys.argv[1:])
    numbers = [int(sys.argv) for (sys.argv) in argument]
    result = sum(numbers)
    print(result)
