#!/bin/usr/python3
from models.base import Base


def checkType(value, attr_1):
    """ Definition """
    # print("CHECK TYPE " + str(value) + " " + str(attr_1))
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(attr_1))
    else:
        return True


def checkValue(value, attr_1):
    """ Definition """
    # print("CHECK VALUE " + str(value) + " " + str(attr_1))
    if value < 0:
        raise ValueError("{} must be >= 0".format(attr_1))
    else:
        return True


class Rectangle(Base):
    """ Definition """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Definition """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self, width):
        """ Definition """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ Definition """
        if checkType(value, "width") and checkValue(value, "width"):
            self.__width = value

    @property
    def height(self):
        """ Definition """
        return self.__height

    @height.setter
    def height(self, value):
        """ Definition """
        if checkType(value, "height") and checkValue(value, "height"):
            self.__height = value

    @property
    def x(self):
        """ Definition """
        return self.__x

    @x.setter
    def x(self, value):
        """ Definition """
        if checkType(value, "x") and checkValue(value, "x"):
            self.__x = value

    @property
    def y(self):
        """ Definition """
        return self.__y

    @y.setter
    def y(self, value):
        """ Definition """
        if checkType(value, "y") and checkValue(value, "y"):
            self.__y = value

    def area(self):
        """ Definition """
        return self.__width * self.__height

    def display(self):
        """Print a rectangle"""
        for k in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for l in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Str overide """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ Definition """
        ls = ["id", "width", "height", "x", "y"]
        for i in range(0, len(args)):
            setattr(self, ls[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)
