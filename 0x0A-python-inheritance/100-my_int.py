#!/usr/bin/python3
"""Contains a class MyInt"""


class MyInt(int):
    """inverted int operators == and !="""

    def __ne__(self, value):
        """revert equal"""
        return (self.real == value)

    def __eq__(self, value):
        """revert not equal"""
        return (self.real != value)
