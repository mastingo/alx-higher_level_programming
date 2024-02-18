#!/usr/bin/python3
"""class square"""

class Square:
    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """property getter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    @property
    def postion(self):
        """prop"""
        return self.__position

    @size.setter
    def position(self, value):
        """prop.set"""
        if type(value) is not tuple and value[0]  > 0 and value[1] > 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """public ares instance"""
        return self.__size * self.__size

    def my_print(self):
        """public area instance"""
        if self.__size == 0:
            print()
            return


        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
