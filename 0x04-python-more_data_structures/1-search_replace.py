#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for index in range(0, len(new_list)):
        if new_list[index] == search:
            new_list[index] = replace
    return new_list
