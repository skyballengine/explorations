import unittest

from exercise_2 import Employee, SeniorEmployee


class Exercise2Test(unittest.TestCase):
    def test_employee(self):
        emp_1 = Employee("Tommy", 50_000)
        self.assertIsInstance(emp_1, Employee)

    def test_senior_employee(self):
        s_emp_1 = SeniorEmployee("Otis", 75_000)
        self.assertEqual(s_emp_1, SeniorEmployee)
