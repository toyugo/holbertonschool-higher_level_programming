#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ Readfile """
    with open(filename, mode="r") as f:
        for line in f.readlines():
            print(line, end="")
