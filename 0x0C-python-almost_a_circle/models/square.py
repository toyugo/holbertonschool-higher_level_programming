#!=/bin/usr/python3
""" Definition of the function """
from models.rectangle import Rectangle
from models.rectangle import checkValue
from models.rectangle import checkType


class Square(Rectangle):
    """ Definition of the function """

    def __init__(self, size, x=0, y=0, id=None):
        """ Definition of the function """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.__width
        # why not return self.size

    @size.setter
    def size(self, value):
        """ Definition of the function """
        checkValue(value, "width")
        checkType(value, "width")
        self.__width = value
        self.__height = value
        self.__size = value

    # why it only work assigned as private class attribute
    def __str__(self):
        """ Definition of the function """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.__size)