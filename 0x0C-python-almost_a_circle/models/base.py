#!/usr/bin/python3
""" Definition of the function """
import json


class Base():
    """ Definition of the function """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Definition of the function """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Definition of the function """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            string_repr = json.dumps(list_dictionaries)
        return (string_repr)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Definition of the function """
        if list_objs is None:
            jsonfile.write("[]")
        else:
            string_repr = []
            for obj in list_objs:
                string_repr.append(obj.to_dictionary())
        json_converted = Base.to_json_string(string_repr)
        with open(cls.__name__ + ".json", "w") as jsonfile:
            jsonfile.write(json_converted)
