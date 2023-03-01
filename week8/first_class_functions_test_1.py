import unittest
from first_class_exercises import greeting, shout


class UnitTests(unittest.TestCase):
    def test_greeting_function_returns_decorated_output(self):
        self.assertEqual(greeting("Python"), "Hello Python")

    def test_shout_function_accepts_a_function_and_a_name_and_does_the_thing(self):
        # define a function that we can pass to shout
        def testFunction(name):
            return ("Hello " + name)

        self.assertEqual(shout(testFunction, "Martin"), "HELLO MARTIN")
