# test_main.py

import unittest
from test import add 
from test import subtract

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
class TestSubFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(subtract(2, 3), -1)

    def test_add_negative_numbers(self):
        self.assertEqual(subtract(-1, -1), -2)
if __name__ == "__main__":
    unittest.main()


