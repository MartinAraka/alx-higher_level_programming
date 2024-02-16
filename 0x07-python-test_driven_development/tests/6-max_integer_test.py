#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_all_OK(self):
        self.assertEqual(max_integer([1, 2, 56]), 56)
        self.assertEqual(max_integer([56, 21, 5]), 56)
        self.assertEqual(max_integer([3, 2, 3.50, 3.51]), 3.51)
        self.assertEqual(max_integer([26.00, 16.14, 26.91, 21.78]), 26.91)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_wrong_type(self):
        self.assertRaises(TypeError, max_integer, [1, 5, 'x'])
        self.assertEqual(max_integer((1, 5, 3)), 5)
        self.assertEqual(max_integer(('z', 'q', 's')), 'z')
