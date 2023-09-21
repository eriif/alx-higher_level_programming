#!/usr/bin/python3
"""Defines unittests for models/square.py.

Unittest classes:
TestSquare_instantiation - line 24
TestSquare_size - line 88
TestSquare_x - line 166
TestSquare_y - line 238
TestSquare_order_of_initialization - line 306
TestSquare_area - line 322
TestSquare_stdout - line 343
TestSquare_update_args - line 426
TestSquare_update_kwargs - line 538
TestSquare_to_dictionary - 640
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """the body of the class"""


def test_init_success(self):
    s1 = Square(5)
    s2 = Square(10)
    self.assertEqual(s1.id, 5)
    self.assertEqual(s2.id, 6)


def test_init_without_args(self):
    self.assertRaises(TypeError, Square)


if __name__ == '__main__':
    unittest.main()
