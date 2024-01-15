#!/usr/bin/python3
import sys
import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the scv serialisation of a list of objects to a file"""
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns list of classes instantiatied from a csv file"""
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                new_list_dict = []
                converted_dict = {}

                for d in list_dicts:
                    for key, value in d.items():
                        converted_dict[key] = int(value)
                    new_list_dict.append(converted_dict)
                list_dicts = new_list_dict
                list_of_instances = []

                for d in list_dicts:
                    list_of_instances.append(cls.create(**d))
                return list_of_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws all rectangles and squares using the turtle model"""
        turt = turtle.Turtle()
        turt.screen.bgcolor(#ccc2c8)
        turt.pensize(4)
        turt.shape("turtle")

        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3cd")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
