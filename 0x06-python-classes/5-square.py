#!/usr/bin/python3
""" Square """


class Square:
    """ Square
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

    def area(self):
        """ Returns area of the square """
        return self.__size ** 2

    @property
    def size(self):
        """ Returns the size of the sqaure """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Prints the square """
        if self.__size == 0:
            print("")
        for column in range(0, self.__size):
            for row in range(0, self.__size):
                print("#", end="")
            print("")
