#!/usr/bin/python3
""" Append to file """


def append_write(filename="", text=""):
    """ Appends given text into a file """
    with open(filename, "a+") as file:
        return file.write(text)
