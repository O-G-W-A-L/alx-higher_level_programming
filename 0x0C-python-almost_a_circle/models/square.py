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

    @property
    def size(self):
        """returns size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of the size"""
        self.width = value
        self.height = value

    def updated(self, *args, **kwargs):
        """assign args to attr based on posiiton"""
        if args:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.size = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """Returns dict rep of the square"""
        square_dict = {"id":self.id, "size":self.width, "x":self.x, "y":self.y}
        return square_dict
