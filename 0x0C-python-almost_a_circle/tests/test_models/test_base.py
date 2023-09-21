#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
TestBase_instantiation - line 21
TestBase_to_json_string - line 108
TestBase_save_to_file - line 154
TestBase_from_json_string - line 232
TestBase_create - line 286
TestBase_load_from_file - line 338
TestBase_save_to_file_csv - line 404
TestBase_load_from_file_csv - line 482
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_initialization(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_saving_id(self):
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_to_json_string_valid(self):
        pass


if __name__ == '__main__':
    unittest.main()
