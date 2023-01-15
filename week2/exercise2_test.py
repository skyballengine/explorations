import unittest
from exercise2 import multiply_3_numbers


class Multiply3FunctionTest(unittest.TestCase):
    def test_1(self):
        result = multiply_3_numbers(1, 2, 3)
        self.assertEqual(result, 6, "Not equal")

    def test_2(self):
        result = multiply_3_numbers(1.5, 5.5, 100.1)
        self.assertIsInstance(result, float, "Result is not of type float")

    def test_3(self):
        result = multiply_3_numbers(-1, 0, 1000)
        self.assertEqual(result, 0, "Result is not 0")


if __name__ == "__main__":
    unittest.main()
