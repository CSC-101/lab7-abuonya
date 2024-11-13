import unittest

import convert

class TestCases(unittest.TestCase):
    # Task 1

    def test_str_to_float1(self):
        input = "72.2"
        result = convert.str_to_float(input)
        expected = 72.2
        self.assertEqual(expected, result)

    def test_str_to_float2(self):
        input = "meow"
        result = convert.str_to_float(input)
        expected = None
        self.assertEqual(expected, result)

    def test_str_to_float3(self):
        input = "143C@ts"
        result = convert.str_to_float(input)
        expected = None
        self.assertEqual(expected, result)