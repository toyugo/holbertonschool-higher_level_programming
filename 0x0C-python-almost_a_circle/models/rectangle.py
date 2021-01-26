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

class Rectangle(Base):
    """
        Simulates a real life Rectangle
        private instance attributes:
            __width
            __height
            __x
            __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Definition of the function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for widh attribute"""
        return self.__width

    @width.setter
    def width(self, val):
        """Setter for widh attribute"""
        # strict_positive_integer_validator('width', val)
        self.__width = val

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, val):
        """Setter for height attribute"""
        # strict_positive_integer_validator('height', val)
        self.__height = val

    @property
    def x(self):
        """Getter for height attribute"""
        return self.__x

    @x.setter
    def x(self, val):
        """Setter for height attribute"""
        # positive_integer_validator('x', val)
        self.__x = val

    @property
    def y(self):
        """Getter for height attribute"""
        return self.__y

    @y.setter
    def y(self, val):
        """Setter for height attribute"""
        # positive_integer_validator('y', val)
        self.__y = val
