import unittest

from exercise_1 import Bird, Duck


class Exercise1Test(unittest.TestCase):
    def test_bird_call(self):
        tom = Bird()
        self.assertEqual(tom.call(), 'chirp')

    def test_duck_call(self):
        sky = Duck()
        self.assertEqual(sky.call(), "quack")


if __name__ == "__main__":
    unittest.main()
