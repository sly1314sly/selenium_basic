import unittest
from selenium import webdriver
from po.loginPage import LoginPage
import os
import time

from ddt import ddt,data,unpack

def get_userInfo():  #加上这个，运行了多条用例
    return [["testuser1","123456"], ["testuser2","123456"]]

@ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    
    def setUp(self): #每个用例之前都要做的操作，输入网址
        driver = self.driver
        driver.get('http://39.107.96.138:3000/signin')


    def tearDown(self): #清除cookies，每个用例之后要做的操作
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):  #最后要做的操作，退出
        cls.driver.quit()


    @data(*get_userInfo())
    @unpack
    def test_login_success(self,username,password):
        driver = self.driver
        lg = LoginPage(driver)

        lg.input_username(username)
        lg.input_password(password)
        lg.click_login_btn()
        text = lg.get_login_result(True)

        self.assertEqual(text,username,'用户名验证错误')

    @unittest.skip('skip')   #跳过该用例，不执行此用例
    def test_login_fail(self):
        driver = self.driver
        lg = LoginPage(driver)

        lg.input_username('1223user1')
        lg.input_password('123456')
        lg.click_login_btn()
        text = lg.get_login_result(False)

        self.assertEqual(text,'用户名或密码错误','错误提示信息验证错误')
