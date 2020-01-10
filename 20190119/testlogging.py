import unittest
import logging


#https://blog.csdn.net/weixin_34149796/article/details/94541352 学习文档


# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logger = logging.getLogger('www')
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)


FORMAT = '%(asctime)-15s  %(action)s %(message)s'
logging.basicConfig(format = FORMAT,filename='example.log',level=logging.WARNING)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # d = {'clientip': '192.168.0.1', 'user': 'user1','action':'test'}
        # logger.warning('test_upper:', extra=d)
        d = {'action':'test'}
        logging.warning('test_upper:', extra=d)        
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        # print('test_isupper is running')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        # print('test_split is running')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
