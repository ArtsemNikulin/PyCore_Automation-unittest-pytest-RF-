"""Calculator tests"""

import unittest
from tasks.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test suite for the Calculator"""

    def setUp(self):
        """Set up the test environment"""
        self.calculator = Calculator()

    def test_sum(self):
        """Test the sum method"""
        self.assertEqual(self.calculator.sum(1, 2), 3)
        self.assertEqual(self.calculator.sum(-1, 1), 0)
        self.assertEqual(self.calculator.sum(-1, -1), -2)
        self.assertEqual(self.calculator.sum(1.5, 2.5), 4.0)

    def test_multiply(self):
        """Test the multiply method"""
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)
        self.assertEqual(self.calculator.multiply(1.5, 2), 3.0)

    def test_subtract(self):
        """Test the subtract method"""
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(1.5, 0.5), 1.0)

    def test_divide(self):
        """Test the divide method"""
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-4, 2), -2)
        self.assertEqual(self.calculator.divide(-4, -2), 2)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        self.assertEqual(self.calculator.divide(10, 0), None)

    def test_sqrt(self):
        """Test the sqrt method"""
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertAlmostEqual(self.calculator.sqrt(2), 1.41)
        with self.assertRaises(ValueError):
            self.calculator.sqrt(-1)

    def test_pi(self):
        """Test the pi method"""
        self.assertAlmostEqual(self.calculator.pi(10), 0.17)


if __name__ == "__main__":
    unittest.main()
