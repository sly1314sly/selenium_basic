import unittest
from test.cases.case2 import LoginTest


def get_suite():
    testsuite = unittest.TestSuite()

    loader2 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

    testsuite.addTests(loader2)

    return testsuite

if __name__ == "__main__":
    suite = get_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)