#!/usr/bin/python3
""" Base """
import json


class Base:
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w+") as file:
            file.write(Base.to_json_string(list_dictionaries))

    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance will all attributes set """
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from the respective file"""
        list_instances = []
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_string = file.readline()
                json_list = Base.from_json_string(json_string)
                for dictionary in json_list:
                    list_instances.append(cls.create(**dictionary))
        except FileNotFoundError:
            pass
        return list_instances
