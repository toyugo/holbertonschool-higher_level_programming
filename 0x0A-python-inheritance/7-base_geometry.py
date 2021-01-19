#!/usr/bin/python3
"""
This module create the look up function
"""


class BaseGeometry():
    """ Base Geometry """
    def area(self):
        """ Area """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ integer_validator """
        if isinstance(value, int) == False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

