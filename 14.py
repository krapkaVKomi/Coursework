import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = 4 * 3
        self.assertEqual(result, 12)
