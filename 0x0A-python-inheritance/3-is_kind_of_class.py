#!/usr/bin/python3
""" Is kind of class """


def is_kind_of_class(obj, a_class):
    """ Returns True if obj is an instance of, or if obj is an isntance of a
    class that inhereted from the specified class, or False otherwise. """
    if isinstance(obj, a_class):
        return True
    else:
        return False
