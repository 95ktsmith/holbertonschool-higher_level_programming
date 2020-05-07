#!/usr/bin/python3


def common_elements(set_1, set_2):
    elements = []
    for element_1 in set_1:
        if element_1 in set_2:
            elements.append(element_1)

    return elements
