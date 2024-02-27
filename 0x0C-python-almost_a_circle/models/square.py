#!/usr/bin/python3
"""importing class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """sub class square with init"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """str override"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        for arg in args:
            if arg is not None:
                if len(args) > 0:
                    self.id = args[0]
                if len(args) > 1:
                    self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                if len(args) > 3:
                    self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        return dict(id=self.id, size=self.size, x=self.x, y=self.y)
