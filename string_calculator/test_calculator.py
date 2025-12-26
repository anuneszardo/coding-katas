import unittest
from decimal import Decimal

from string_calculator.calculator import string_calculator


class TestCalculator(unittest.TestCase):
    def test_string_calculator_returns_integer(self):
        self.assertEqual(string_calculator("1"), 1)

    def test_string_calculator_returns_negative_integer(self):
        self.assertEqual(string_calculator("-1"), -1)

    def test_string_calculator_returns_stripped(self):
        self.assertEqual(string_calculator(" -1"), -1)

    def test_string_calculator_returns_zero_number(self):
        self.assertEqual(string_calculator("0"), 0)

    def test_string_calculator_returns_sum_of_values(self):
        self.assertEqual(string_calculator("1+1"), 2)

    def test_string_calculator_returns_decrease_of_values(self):
        self.assertEqual(string_calculator("1-1"), 0)

    def test_string_calculator_returns_sum_of_negative_positive_values(self):
        self.assertEqual(string_calculator(" +5-6"), -1)

    def test_string_calculator_returns_negative_positive_values_multiplied(self):
        self.assertEqual(string_calculator("+5*-6"), -30)

    def test_string_calculator_returns_values_divided(self):
        self.assertEqual(string_calculator("15/5"), 3)

    def test_string_calculator_returns_decimals(self):
        self.assertAlmostEqual(string_calculator("10/3"), Decimal('3.333333333333333481363069950020872056484222412109375'))

