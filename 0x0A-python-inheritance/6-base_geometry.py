#!/usr/bin/python3
"""Writing a  base geometry class"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
