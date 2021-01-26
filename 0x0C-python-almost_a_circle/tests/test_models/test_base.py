#!/usr/bin/python3
""" Project: Python Almost a Circle """
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):
    """ Unit test Base class """
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
    def test_id(self):
        # compare argument 1 avec argument 2 et verifie le resultat)
        self.assertEqual(self.r1.id, 1)
        print(self.r2.id)
        self.assertEqual(self.r2.id, 2)
        print(self.r3.id, 12)
        
