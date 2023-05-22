import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)

class AnotherTestCase(unittest.TestCase):
    def test_multiplication(self):
        result = 4 * 3
        self.assertEqual(result, 12)

# Створення тестового набору і додавання тестових класів
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(MyTestCase))
test_suite.addTest(unittest.makeSuite(AnotherTestCase))

# Запуск тестів
unittest.TextTestRunner().run(test_suite)
