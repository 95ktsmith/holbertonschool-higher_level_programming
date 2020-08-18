#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers
        Uses (maybe a poor implementation of) binary search
    """
    # If list is None or empty
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    # Set index to center of the list to start testing
    index = int(len(list_of_integers) / 2)

    # If index is the first number, only check right of it
    if index == 0:
        if list_of_integers[index] > list_of_integers[index + 1]:
            return list_of_integers[index]
    # If index is the last number, only check left of it
    elif index == len(list_of_integers) - 1:
        if list_of_integers[index] > list_of_integers[index - 1]:
            return list_of_integers[index]
    else:
        # If left number is bigger, repeat this function on left half of list
        if list_of_integers[index - 1] > list_of_integers[index]:
            return find_peak(list_of_integers[:index])
        # If right number is bigger, repeat this function on right half of list
        elif list_of_integers[index + 1] > list_of_integers[index]:
            return find_peak(list_of_integers[index - 1:])
        # If neither is bigger, index is a peak
        else:
            return list_of_integers[index]
