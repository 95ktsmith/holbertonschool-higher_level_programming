#!/usr/bin/python3
def pow(a, b):
    result = 1

    if b < 0:
        for pows in range(b, 0):
            result *= a
        return 1 / result
    else:
        for pows in range(0, b):
            result *= a
        return result
