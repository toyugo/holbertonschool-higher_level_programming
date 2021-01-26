from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseID(TestCase):
    """Test Base id."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        self.assertEqual(Base(15).id,15)
        self.assertEqual(Base().id, 1)
