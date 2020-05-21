#!/usr/bin/python3
""" Square """


class Square:
    """ A square

    Attributes:
        __size (int): Size of the square
    """
    __size = 0

    def __init__(self, size=0):
        """ Init """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
