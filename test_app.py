"""Unit tests for the calculator app."""

import unittest

from app import add, subtract


class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(add(-1, 3), 2)


class TestSubtract(unittest.TestCase):
    def test_subtract_basic(self):
        self.assertEqual(subtract(5, 1), 4)

    def test_subtract_resulting_in_negative(self):
        self.assertEqual(subtract(3, 7), -4)


if __name__ == "__main__":
    unittest.main()
