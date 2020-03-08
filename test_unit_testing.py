import unittest
import unit_testing

class TestUnitTesting(unittest.TestCase):
    def test_add(self):
        result = unit_testing.add(10,5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = unit_testing.subtract(10,5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        self.assertEqual(unit_testing.multiply(10,5), 50)
        self.assertEqual(unit_testing.multiply(10, 0), 0)
        self.assertEqual(unit_testing.multiply(10, -5), -50)
        self.assertEqual(unit_testing.multiply(-10, -5), 50)

    def test_divide(self):
        self.assertEqual(unit_testing.divide(10, 5), 2)
        self.assertEqual(unit_testing.divide(0, 5), 0)
        self.assertEqual(unit_testing.divide(-10, 5), -2)
        self.assertEqual(unit_testing.divide(10, -5), -2)
        self.assertEqual(unit_testing.divide(-10, -5), 2)
        # testing exceptions
        self.assertRaises(ValueError, unit_testing.divide, 10,0)
        # alternative solution for testing exceptions using context manager:
        with self.assertRaises(ValueError):
            unit_testing.divide(10,0)

if __name__ == '__main__':
    unittest.main()
