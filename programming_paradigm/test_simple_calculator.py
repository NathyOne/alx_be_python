import unittest
from simple_calculator import SimpleCalculator


class simple_calculator_test(unittest.TestCase):
    def test_addition(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_subtraction(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_division(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_multiplication(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.multiply(10, 5), 50)
