#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square."""

    def __init__(self, size):
        """ Init  """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ print """
        return "[Square] {}/{}".format(self.__size, self.__size)
