#!/usr/bin/python3


class Base():
    """ Definition """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Definition """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
