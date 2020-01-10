#参考文档：https://selenium-python.readthedocs.io/page-objects.html


import unittest

from selenium import webdriver
from page import LoginPage

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        username = 'testuser1'
        password = '123456'
        lg = LoginPage(self.driver,username,password)
        lg.login()

        result_name = lg.get_login_name()
        self.assertEqual(result_name,username)        #断言

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)