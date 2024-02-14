#!/usr/bin/python3
"""Square Module

Inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Has Rectangle as its super class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Init method

        Initializes new instances of square
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Str method"""
        return (f'[Square] ({self.id}) {self.x}/{self.y} '
                f'- {self.height}')

    @property
    def size(self):
        """public getter and setter for size"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update method"""
        keys = ['id', 'size', 'x', 'y']
        keyset = set()
        if args:
            for key, value in zip(keys, args):
                if hasattr(self, key):
                    setattr(self, key, value)
                    keyset.add(key)
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key) and key not in keyset:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Converts square instance to dictionaty"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
