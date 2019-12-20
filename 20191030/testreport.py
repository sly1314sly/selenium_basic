import unittest
import HTMLReport

from testcase2.test1 import TestStringMethods1
from testcase2.test4 import TestStringMethods4
import testcase2




def suite1():   #运行了所有的
    suite = unittest.TestSuite()
    loader = unittest.TestLoader().discover('testcase2',pattern ='test*.py')
    suite.addTests(loader)
    return suite

def suite2():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods1)
    loader2 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods4)

    suite.addTests(loader)
    suite.addTests(loader2)
    return suite

if __name__ == '__main__':
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite1())
    suite = suite2()
    
    test_runner = HTMLReport.TestRunner(report_file_name='index',
                                        output_path='report',
                                        title='一个简单的测试报告',
                                        description='随意描述',
                                        thread_count=10,
                                        thread_start_wait=0,
                                        # tries=5,
                                        # delay=1,
                                        # back_off=2,
                                        # retry=False,
                                        sequential_execution=True,
                                        lang='cn'
                                        )
    test_runner.run(suite)