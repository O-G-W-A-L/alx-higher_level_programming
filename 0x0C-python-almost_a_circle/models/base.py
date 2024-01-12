#!/usr/bin/python3
import sys
import os
import json
import csv


"""Defines a base model class"""

class Base:
    """Represents the base model"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns list of dict to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_json = json.dumps(list_dictionaries)

        return to_json

    @classmethod
    def save_to_file(cls, list_objs):
        """write the json string rep of list_objs to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns list of json string rep"""
        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attr already set"""
        if dictionary and dictionary != []:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r") as file:
                list_dicts = Base.from_json_string(file.read())
            list_instances = []

            for d in list_dicts:
                list_instances.append(cls.create(**d))
            return list_instances
        except FileNotFoundError:
            return []
