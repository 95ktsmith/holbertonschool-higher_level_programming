#!/usr/bin/python3
""" Is Same Class """


def is_same_class(obj, a_class):
    """ Returns True if obj is an instance of a_class, false otherwise """
    if type(obj) is a_class:
        return True
    else:
        return False
