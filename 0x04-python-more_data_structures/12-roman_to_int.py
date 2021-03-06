#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    decimal = 0
    numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for idx in range(0, len(roman_string)):
        if idx + 1 < len(roman_string) and\
                numeral[roman_string[idx]] < numeral[roman_string[idx + 1]]:
            decimal -= numeral[roman_string[idx]]
        else:
            decimal += numeral[roman_string[idx]]
    return decimal
