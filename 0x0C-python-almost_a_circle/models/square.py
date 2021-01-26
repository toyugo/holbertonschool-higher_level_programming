#!=/bin/usr/python3
from models.rectangle import Rectangle
from models.rectangle import checkValue
from models.rectangle import checkType


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.__width
        # why not return self.size

    @size.setter
    def size(self, value):
        checkValue(value, "width")
        checkType(value, "width")
        self.__width = value
        self.__height = value
        self.__size = value

    # why it only work assigned as private class attribute
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.__size)
