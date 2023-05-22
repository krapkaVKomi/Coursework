import unittest

class CustomTestResult(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results.append((test, 'pass'))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.results.append((test, 'fail'))

    def addError(self, test, err):
        super().addError(test, err)
        self.results.append((test, 'error'))

# Використання CustomTestResult для збору звіту
test_result = CustomTestResult()
test_suite.run(test_result)

# Виведення звіту
for test, result in test_result.results:
    print(f'Test: {test} Result: {result}')
