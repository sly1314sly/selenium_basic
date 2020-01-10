import unittest
import sys


class MyTestCase(unittest.TestCase):
    
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(sys.platform.startswith('win'), 
                     "run in this library version") #如果是windows系统就支持运行
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows") #skipUnless除非是windows就执行
    def test_windows_support(self):
        # windows specific testing code
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)