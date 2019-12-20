import unittest

from testcase2.test1 import TestStringMethods1
from testcase2.test4 import TestStringMethods4





def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods1('test_upper1'))
    suite.addTest(TestStringMethods4('test_split4'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
