import unittest

from exercise_2 import Employee, SeniorEmployee


class Exercise2Test(unittest.TestCase):
    def test_employee(self):
        emp_1 = Employee("Tommy", 50_000)
        self.assertIsInstance(emp_1, Employee)

    def test_senior_employee(self):
        s_emp_1 = SeniorEmployee("Otis", 75_000)
        self.assertIsInstance(s_emp_1, SeniorEmployee)

    def test_get_name(self):
        emp_1 = Employee("Tommy", 50_000)
        s_emp_1 = SeniorEmployee("Otis", 75_000)
        emp_1_name = emp_1.get_name()
        s_emp_1_name = s_emp_1.get_name()
        self.assertEqual(emp_1_name, "Tommy")
        self.assertEqual(s_emp_1_name, "Otis")

    def test_get_salary(self):
        emp_1 = Employee("Tommy", 50_000)
        s_emp_1 = SeniorEmployee("Otis", 75_000)
        emp_1_sal = emp_1.get_salary()
        s_emp_1_sal = s_emp_1.get_salary()
        self.assertEqual(emp_1_sal, 50_000)
        self.assertEqual(s_emp_1_sal, 75_000)

    def test_gross_monthly_pay(self):
        emp_1 = Employee("Tommy", 50_000)
        s_emp_1 = SeniorEmployee("Otis", 75_000)
        emp_1_gmp = emp_1.gross_monthly_pay()
        s_emp_1_gmp = s_emp_1.gross_monthly_pay()
        self.assertEqual(emp_1_gmp, 50_000 / 12)
        self.assertEqual(s_emp_1_gmp, 75_000 / 12 + 500)




if __name__ == "__main__":
    unittest.main()
