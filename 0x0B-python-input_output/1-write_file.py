#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    Function that writes a string to a text
    file (UTF8) and returns the number of characters written
    """
    cp = 0
    with open(filename, mode="r") as f:
        for line in f.readlines():
            for c in line:
                cp += 1
    return(cp)
