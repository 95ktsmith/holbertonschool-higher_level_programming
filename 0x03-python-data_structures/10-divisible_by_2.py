#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None

    even_list = my_list[:]
    for index in range(0, len(my_list)):
        if my_list[index] % 2 == 0:
            even_list[index] = True
        else:
            even_list[index] = False

    return even_list
