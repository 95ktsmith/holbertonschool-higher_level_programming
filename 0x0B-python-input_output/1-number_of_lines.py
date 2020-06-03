#!/usr/bin/python3
""" Number of lines """


def number_of_lines(filename=""):
    """ Returns the number of lines in a file """
    lines = 0
    with open(filename) as file:
        for line in file:
            lines += 1
    return lines
