#!/usr/bin/python3
""" Definition of the function """
from models.base import Base


class Rectangle(Base):
    """ Definition of the function """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Definition of the function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self, width):
        """ Definition of the function """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ Definition of the function """
        self.__width = value

    @property
    def height(self):
        """ Definition of the function """
        return self.__height

    @height.setter
    def height(self, value):
        """ Definition of the function """
        # if checkType(value, "height") and checkValueHeight(value, "height"):
        self.__height = value

    @property
    def x(self):
        """ Definition of the function """
        return self.__x

    @x.setter
    def x(self, value):
        """ Definition of the function """
        # if checkType(value, "x") and checkValue(value, "x"):
        self.__x = value

    @property
    def y(self):
        """ Definition of the function """
        return self.__y

    @y.setter
    def y(self, value):
        """ Definition of the function """
        # if checkType(value, "y") and checkValue(value, "y"):
        self.__y = value
