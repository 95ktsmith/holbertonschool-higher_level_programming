#!/usr/bin/python3
""" Rectangle Model """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init
            Uses Base's init for setting id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x Setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y Setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area of the instance """
        return self.__width * self.__height

    def display(self):
        """ Displays instance as made of #'s """
        s = ("\n" * self.__y)\
            + ((" " * self.__x) + ("#" * self.__width) + "\n") * self.__height
        print(s[:-1])

    def __str__(self):
        """ Returns a string representation of the instance
            ex. [Rectangle] (id) x/y - width/height
        """
        s = "[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/"\
            + str(self.__y) + " - " + str(self.__width) + "/"\
            + str(self.__height)
        return s

    def update(self, *args, **kwargs):
        """ Updates attributes of the instance in order:
        (id, width, height, x, y)
        If args is None or empty, kwargs will be used instead.
        """
        if args is None or len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            atts = ['id', 'width', 'height', 'x', 'y']
            for index in range(0, len(args)):
                setattr(self, atts[index], args[index])

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
