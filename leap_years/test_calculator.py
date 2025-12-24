import unittest

from leap_years.calculator import calculate_leap_year


class TestCalculator(unittest.TestCase):
    def test_leap_years_with_integer(self):
        leap_years = calculate_leap_year(1996)
        assert leap_years is True

    def test_leap_years_with_decimal(self):
        with self.assertRaises(TypeError):
            calculate_leap_year(1.0)

    def test_leap_years_with_no_years(self):
        with self.assertRaises(TypeError):
            calculate_leap_year(None)

    def test_leap_years_not_leap_year(self):
        leap_years = calculate_leap_year(2001)
        assert leap_years is False

    def test_atypical_leap_years(self):
        assert calculate_leap_year(1900) is False
        assert calculate_leap_year(2000) is True