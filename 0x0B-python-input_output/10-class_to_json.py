#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure for
    JSON serialization of an object """
    my_dict = {}
    for attribute, value in obj.__dict__.items():
        if type(value) in [list, dict, str, int, bool]:
            my_dict[attribute] = value
    return my_dict
