#!/usr/bin/python3
""" Geometry base Class """


class BaseGeometry:
    """ BaseGeometry Class """
    def area(self):
        """ Prints area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates that value is an integer greater than 0 """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
