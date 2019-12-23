import unittest
from test.cases.case2 import LoginTest
from test.cases.case3 import RegisterTest

def get_suite():
    testsuite = unittest.TestSuite()

    # loader = unittest.TestLoader().discover(start_dir='test',pattern='case*.py')
    # testsuite.addTests(loader)

    loader2 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # loader3 = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)
    # testsuite.addTests(loader2)
    testsuite.addTests(loader2)

    return testsuite

if __name__ == "__main__":
    suite = get_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)