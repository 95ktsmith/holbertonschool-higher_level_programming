#!/usr/bin/python3
""" A Rectangle """


class Rectangle:
    """ A Rectangle """
    number_of_instances = 0
    print_symbol = "#"
    __height = 0
    __width = 0

    def __str__(self):
        """ string representation of the Rectangle
            If either width or height are 0, returns an empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (((str(self.print_symbol) * self.__width) + "\n") *
                    self.__height)[:-1]

    def __repr__(self):
        """ represention of the Rectangle """
        return "Rectangle(" + str(self.__width) + ", " \
            + str(self.__height) + ")"

    def __init__(self, width=0, height=0):
        """ Init
            width and height need to be integers greater than or
            equal to zero
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        Rectangle.number_of_instances += 1

    def __del__(self):
        """ del """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the rectangle (width x height) """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the peremiter of the rectangle ( width*2 + height *2)
            If either width or heigth are 0, perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def bigger_or_equal(rect_1, rect_2):
        """ Returns the bigger of two rectangles based on area, or
            the first rectangle if the two are equal.
            rect_1 and rect_2 must be Rectangles.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
