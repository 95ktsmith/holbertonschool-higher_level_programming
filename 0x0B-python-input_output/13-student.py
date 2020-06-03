#!/usr/bin/python3
""" Student """


class Student:
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ Init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary representation of an instance """
        my_dict = {}
        if type(attrs) is list and all(type(elem) is str for elem in attrs):
            for attribute, value in self.__dict__.items():
                if attribute in attrs and\
                        type(value) in [list, dict, str, int, bool]:
                    my_dict[attribute] = value
        else:
            for attribute, value in self.__dict__.items():
                if type(value) in [list, dict, str, int, bool]:
                    my_dict[attribute] = value
        return my_dict

    def reload_from_json(self, json):
        """ Replaces all attributes of the instance with those in json dict """
        for key in json:
            self.key = json[key]
