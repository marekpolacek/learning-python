import unittest
from unittest.mock import patch
from unit_testing import Employee

class TestEmployee(unittest.TestCase):

    # run once at the beginning of the test
    @classmethod
    def setUpClass(cls):
        print('setup class')

    # run once at the end of the test
    @classmethod
    def tearDownClass(cls):
        print('tear down class')

    # run at the beginning of each test
    def setUp(self):
        # run before every single test
        self.employee_1 = Employee('John', 'Doe', 70000)
        self.employee_2 = Employee('Jane', 'Doe', 80000)

    # run at the end of each test
    def tearDown(self):
        # run after every single test
        pass

    def test_email(self):
        self.assertEqual(self.employee_1.email,'John.Doe@email.com')
        self.assertEqual(self.employee_2.email, 'Jane.Doe@email.com')
        self.employee_1.first = 'Peter'
        self.employee_2.first = 'Sue'
        self.assertEqual(self.employee_1.email, 'Peter.Doe@email.com')
        self.assertEqual(self.employee_2.email, 'Sue.Doe@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee_1.fullname,'John Doe')
        self.assertEqual(self.employee_2.fullname, 'Jane Doe')
        self.employee_1.first = 'Peter'
        self.employee_2.first = 'Sue'
        self.assertEqual(self.employee_1.fullname, 'Peter Doe')
        self.assertEqual(self.employee_2.fullname, 'Sue Doe')

    def test_apply_raise(self):
        self.assertEqual(self.employee_1.email,'John.Doe@email.com')
        self.assertEqual(self.employee_2.email, 'Jane.Doe@email.com')
        self.employee_1.apply_raise()
        self.employee_2.apply_raise()
        self.assertEqual(self.employee_1.pay, 77000)
        self.assertEqual(self.employee_2.pay, 88000)

    def test_monthly_schedule(self):
        with patch('unit_testing.requests.get') as mocked_get:
            # successful response
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.employee_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Doe/May')
            self.assertEqual(schedule, 'Success')

            # bad response
            mocked_get.return_value.ok = False
            schedule = self.employee_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Doe/June')
            self.assertEqual(schedule, 'Bad response')

if __name__ == '__main__':
    unittest.main()