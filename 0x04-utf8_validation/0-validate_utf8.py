#!/usr/bin/python3
"""
A python function
"""


def validUTF8(data):
    """
    Determines if a given data set represents
    a valid UTF-8 encoding
    data: data set to be checked
    Returns:
        true if valid UTF-8 false otherwise
    """
    no_of_bytes = 0

    for k in data:
        if no_of_bytes == 0:
            if k >> 5 == 0b110 or k >> 5 == 0b1110:
                no_of_bytes = 1
            elif k >> 4 == 0b1110:
                no_of_bytes = 2
            elif k >> 3 == 0b11110:
                no_of_byres = 3
            elif k >> 7 == 0b1:
                return False
        else:
            if k >> 6 != 0b10:
                return False
            no_of_bytes -= 1
    return no_of_bytes == 0
