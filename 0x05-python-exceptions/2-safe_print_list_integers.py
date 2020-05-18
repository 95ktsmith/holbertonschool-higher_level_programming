#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    index = 0
    elemsPrinted = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            elemsPrinted += 1
        except (ValueError, IndexError):
            pass
        finally:
            index += 1

    print("")
    return elemsPrinted
