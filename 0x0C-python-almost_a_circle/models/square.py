#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation """
        s = "[Square] (" + str(self.id) + ") " + str(self.x) + "/"\
            + str(self.y) + " - " + str(self.width)
        return s

    @property
    def size(self):
        """ Size Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates attributes of the instance in order:
        (id, size, x, y)
        If args is None or empty, kwargs will be used instead.
        """
        if args is not None and len(args) != 0:
            atts = ['id', 'size', 'x', 'y']
            for index in range(0, len(args)):
                setattr(self, atts[index], args[index])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
