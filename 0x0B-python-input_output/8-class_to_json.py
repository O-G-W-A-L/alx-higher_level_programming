#!/usr/bin/python3
"""Defines a Python class to JSON function"""


def class_to_json(obj):
    """class to json

    Args:
        obj: instance of the class
    """
    return (obj.__dict__)
