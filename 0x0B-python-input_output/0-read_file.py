#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ Reads and prints a file """
    with open(filename) as file:
        print(file.read())
