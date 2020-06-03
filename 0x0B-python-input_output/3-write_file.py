#!/usr/bin/python3
""" Write to file """


def write_file(filename="", text=""):
    """ Writes given text into a file """
    with open(filename, "w+") as file:
        return file.write(text)
