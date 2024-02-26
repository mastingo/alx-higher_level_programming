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
