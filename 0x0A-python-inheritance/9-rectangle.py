#!/usr/bin/python3
""" Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class """

    def __init__(self, width, height):
        """ Init
            width and height must be integers and greater than 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string of [Rectangle] <width>/<height> """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
