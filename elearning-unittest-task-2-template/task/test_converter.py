"""Test for the Converter"""

import unittest
from unittest.mock import patch
from task.converter import Converter


def mock_converter(_, celsius):
    """Mock converter to replace the original convert_celsius_to_fahrenheit method"""
    return celsius * 9.0 / 5.0 + 32


class TestConverter(unittest.TestCase):
    """Test suite for the Converter"""
    def setUp(self):
        """Set up class initialization"""
        self.converter = Converter()

    @patch('task.converter.Converter.convert_celsius_to_fahrenheit', new=mock_converter)
    def test_converter(self):
        """Test the convert_celsius_to_fahrenheit method with the mock_converter"""
        celsius = 100
        expected_fahrenheit = 212
        result = self.converter.convert_celsius_to_fahrenheit(celsius)
        self.assertEqual(result, expected_fahrenheit)


if __name__ == "__main__":
    unittest.main()
