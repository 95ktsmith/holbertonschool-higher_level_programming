#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0 and len(tuple_b) > 0:
        a = tuple_a[0] + tuple_b[0]
    elif len(tuple_a) > 0:
        a = tuple_a[0]
    elif len(tuple_b) > 0:
        a = tuple_b[0]
    else:
        a = 0

    if len(tuple_a) > 1 and len(tuple_b) > 1:
        b = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) > 1:
        b = tuple_a[1]
    elif len(tuple_b) > 1:
        b = tuple_b[1]
    else:
        b = 0

    return ((a, b))
