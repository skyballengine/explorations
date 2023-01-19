import unittest
from exercise2 import multiply_3_numbers
class OperationFailedError(Exception):
    pass

class Multiply3FunctionTest(unittest.TestCase):
    def test_1(self):
        """Test for equality"""
        result = multiply_3_numbers(1, 2, 3)
        self.assertEqual(result, 6, "Not equal")
        #with self.assertRaises(OperationFailedError):
            #self.assertEqual(result, 7, "Wrong")

    def test_2(self):
        """Test if of type float"""
        result = multiply_3_numbers(1.5, 5.5, 100.1)
        self.assertIsInstance(result, float, "Result is not of type float")
        self.assertAlmostEqual(result, 825.825)

    def test_3(self):
        """Test multiplying with 0"""
        result = multiply_3_numbers(-1, 0, 1000)
        self.assertEqual(result, 0, "Result is not 0")


if __name__ == "__main__":
    unittest.main()
