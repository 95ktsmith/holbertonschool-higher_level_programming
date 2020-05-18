#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elemsPrinted = 0
    while elemsPrinted < x:
        try:
            print(my_list[elemsPrinted], end="")
            elemsPrinted += 1
        except:
            break
    print("")
    return elemsPrinted
