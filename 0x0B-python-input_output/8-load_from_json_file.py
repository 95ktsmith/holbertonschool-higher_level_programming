#!/usr/bin/python3
""" Load object from json file """
import json


def load_from_json_file(filename):
    """ Returns an object loaded from a json file """
    with open(filename) as file:
        return json.loads(file.readline())
