import unittest
from simple_calculator import SimpleCalculator


class simple_calculator_test(unittest.TestCase):
    def test_add(self):
        calculator = SimpleCalculator()
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)

    def test_sub(self):
        calculator = SimpleCalculator()
        result = calculator.subtract(10, 5)
        self.assertEqual(result, 5)
    def test_divide(self):
        calculator = SimpleCalculator()
        result = calculator.divide(10,5)
        self.assertEqual(result, 2)
    def test_mul(self):
        calculator = SimpleCalculator()
        result = calculator.multiply(5, 10)
        self.assertEqual(result, 50)
        





