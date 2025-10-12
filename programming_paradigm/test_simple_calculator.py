import unittest
from simple_calculator import SimpleCalculator


class simple_calculator_test(unittest.TestCase):
    def test_addition(self):
        self.calc = SimpleCalculator()
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtraction(self):
        self.calc = SimpleCalculator()
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_division(self):
        self.calc = SimpleCalculator()
        result = self.calc.divide(10, 5)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        self.calc = SimpleCalculator()
        result = self.calc.multiply(5, 10)
        self.assertEqual(result, 50)
