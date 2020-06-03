#!/usr/bin/python3
""" Read lines """
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """ Prints up to a number of lines from a file, or the entire file if
        nb_lines is <= 0 or greater than the number of lines in the file. """
    with open(filename) as file:
        if nb_lines <= 0 or nb_lines > number_of_lines(filename):
            for line in file:
                print(line, end="")
                if line[-1] != "\n":
                    print()
        else:
            for line in range(0, nb_lines):
                read_line = file.readline()
                print(read_line, end="")
                if read_line[-1] != "\n":
                    print()
