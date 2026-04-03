import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.calculator import add, subtract, multiply, combined, divide


class TestAdd(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(add(3, 4), 7)

    def test_zeros(self):
        self.assertEqual(add(0, 0), 0)

    def test_one_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_negatives(self):
        self.assertEqual(add(-3, -7), -10)

    def test_mixed_sign(self):
        self.assertEqual(add(-3, 7), 4)

    def test_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    def test_large_numbers(self):
        self.assertEqual(add(10**9, 10**9), 2 * 10**9)


class TestSubtract(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_zeros(self):
        self.assertEqual(subtract(0, 0), 0)

    def test_result_negative(self):
        self.assertEqual(subtract(3, 10), -7)

    def test_negatives(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.5), 3.0)

    def test_same_value(self):
        self.assertEqual(subtract(7, 7), 0)


class TestMultiply(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_zero(self):
        self.assertEqual(multiply(0, 100), 0)

    def test_both_zeros(self):
        self.assertEqual(multiply(0, 0), 0)

    def test_negatives(self):
        self.assertEqual(multiply(-3, -4), 12)

    def test_mixed_sign(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)

    def test_by_one(self):
        self.assertEqual(multiply(99, 1), 99)


class TestCombined(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(combined(2, 3), 10)

    def test_zeros(self):
        self.assertEqual(combined(0, 0), 0)

    def test_negatives(self):
        self.assertEqual(combined(-2, -3), 2)

    def test_floats(self):
        self.assertAlmostEqual(combined(1.0, 2.0), 4.0)


class TestDivide(unittest.TestCase):

    def test_positive(self):
        self.assertAlmostEqual(divide(10, 2), 5.0)

    def test_floats(self):
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)

    def test_negative_numerator(self):
        self.assertAlmostEqual(divide(-10, 2), -5.0)

    def test_negative_denominator(self):
        self.assertAlmostEqual(divide(10, -2), -5.0)

    def test_both_negatives(self):
        self.assertAlmostEqual(divide(-10, -2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_zero_numerator(self):
        self.assertAlmostEqual(divide(0, 5), 0.0)


if __name__ == "__main__":
    unittest.main()