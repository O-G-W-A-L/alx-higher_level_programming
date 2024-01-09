#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """save json to text file

    Args:
        my_obj: the python object
        filename: the file to write to
    """
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
