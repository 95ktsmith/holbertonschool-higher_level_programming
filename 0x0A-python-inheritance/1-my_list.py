#!/usr/bin/python3
""" MyList """


class MyList(list):
    """ A Class based on the default list Class """

    def print_sorted(self):
        """ Prints the list in ascending order """
        print(sorted(self))
