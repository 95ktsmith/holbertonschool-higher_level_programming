#!/usr/bin/python3
""" Add integer """


def add_integer(a, b=98):
    """ Adds two integers and returns the result
        a and b must be integers or floats
    """
    import doctest
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
