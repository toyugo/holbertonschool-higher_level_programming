#!/usr/bin/python3
""" Project: Python Almost a Circle """
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):
    """ Unit test Base class """

    def test_id(self):
        self.assertEqual(1, Base().id)
        self.assertEqual(15, Base(15).id)
        self.assertEqual(2, self.Base(None)
