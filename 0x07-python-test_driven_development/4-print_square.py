#!/usr/bin/python3
"""
    Module
"""


def print_square(size):
    """ print"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("\n", end="")
