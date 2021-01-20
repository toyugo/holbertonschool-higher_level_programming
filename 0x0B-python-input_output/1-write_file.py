#!/usr/bin/python3
""" Module """


def write_file(filename="", text=""):
    """
    Function that writes a string to a text
    file (UTF8) and returns the number of characters written
    """
    cp = 0
    with open(filename, mode="w", encoding="utf8") as f:
        f.write(text)
    return(len(text))
