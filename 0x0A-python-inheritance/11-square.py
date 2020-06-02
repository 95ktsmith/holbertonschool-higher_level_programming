#!/usr/bin/python3
""" Square Class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class, inherits from Rectangle """
    def __init__(self, size):
        """ Init
            size must be an integer greater than zero
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ Returns a string of [Square] <size>/<size> """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
