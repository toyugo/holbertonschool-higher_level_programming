#!/usr/bin/python3
""" Module """


def append_write(filename="", text=""):
    """
    function that appends a string
    at the end of a text file (UTF8) and returns the number of characters
    """
    with open(filename, mode="a") as f:
        f.write(text)
    return(len(text))
