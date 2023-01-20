import unittest

from inheritance import Rectangle
from exercise_3 import Carpet


class Exercise3Test(unittest.TestCase):
    def test_carpet(self):
        carpet_1 = Carpet(Rectangle(10, 50), 5.25)
        rect = carpet_1.get_size()
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.area(), 500)
        self.assertEqual(carpet_1.cost(), 2625)


if __name__ == "__main__":
    unittest.main()
