#!/usr/bin/python3
""" Inherits from """


def inherits_from(obj, a_class):
    """ Returns True if obj is an instance of a class that inherited from
    a_class, or False otherwise. """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
