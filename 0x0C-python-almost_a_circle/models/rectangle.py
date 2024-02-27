#!/usr/bin/python3


from models.base import Base


"""rectangle class inheriting from base"""


class Rectangle(Base):
    """initialising rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """super method to access id"""
        super().__init__(id)

    @property
    def width(self):
        """property setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter makes sure var is an int"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """property getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """make sure height is an int"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """property getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """property getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """method to do area fo the rectangle"""
        return self.__width * self.__height

    def display(self):
        """method to display rows and height in #"""
        if self.width == 0 or self.height == 0:
            print('')
            retrun

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """__str__ override to return this f string format"""
        return f"[Rectangle]({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"   # noqa

    def update(self, *args, **kwargs):
        """assign the variables depending on the args index"""
        for arg in args:
            if arg is not None:
                if len(args) > 0:
                    self.id = args[0]
                if len(args) > 1:
                    self.width = args[1]
                if len(args) > 2:
                    self.height = args[2]
                if len(args) > 3:
                    self.x = args[3]
                if len(args) > 4:
                    self.y = args[4]

        for key, value in kwargs.items():
            """handling the keyword args here assigning to the repective"""
            setattr(self, key, value)

    def to_dictionary(self):
        """ method to turn the self variables to a dict"""
        return dict(id = self.id, width = self.width, height =self.height, x = self.x, y= self.y) # noqa
