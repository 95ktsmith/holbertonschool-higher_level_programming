#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    index = 0
    elemsPrinted = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            elemsPrinted += 1
            index += 1
        except ValueError:
            index += 1
        except:
            break

    print("")
    return elemsPrinted
