#!/usr/bin/python3
"""module for square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """square model"""
    def __init__(self, size, x=0, y=0, id=None):
        """square class constructor"""
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """str rep"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
