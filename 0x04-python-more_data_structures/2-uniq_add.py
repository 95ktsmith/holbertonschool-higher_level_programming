#!/usr/bin/python3


def uniq_add(my_list=[]):
    result = 0
    for index in range(0, len(my_list)):
        if my_list[index] not in my_list[0:index]:
            result += my_list[index]

    return result
