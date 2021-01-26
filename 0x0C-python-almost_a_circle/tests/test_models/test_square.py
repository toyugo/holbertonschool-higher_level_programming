import unittest
from models.base import Base
from models.square import Square

class TestRectangle(unittest.TestCase):
    """ Unit test Base class """
    # def __init__(self, size, x=0, y=0, id=None)::
    # attr = ["width", "height", "x", "y"]
    def setUp(self):
        # print(Rectangle.__base__.__dict__)
        Square._Base__nb_objects = 0

    def test_size_negatif(self):
        with self.assertRaises(ValueError) as cm:
            Square(-1, 10, 10)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_x_negatif(self):
        with self.assertRaises(ValueError) as cm:
            Square(10, -2, 10)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_y_negatif(self):
        with self.assertRaises(ValueError) as cm:
            Square(10, 10, -2)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    # ZERO
    def test_size_zero(self):
        with self.assertRaises(ValueError) as cm:
            Square(0, 10, 10)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def BaseSquare(self):
        s1 = Square(5)
        self.assertEqual(s1, "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1, "[Square] (1) 0/0 - 10")
        with self.assertRaises(TypeError) as cm:
            try:
                s1.size = "9"
            except Exception as e:
                print("[{}] {}".format(e.__class__.__name__, e))
        self.assertEqual(str(cm.exception), "width must be an integer")
