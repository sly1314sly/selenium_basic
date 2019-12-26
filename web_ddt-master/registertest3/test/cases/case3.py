##注册用例

   
import unittest
from selenium import webdriver
from po.registerPage import registerPage
import os
import time


class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    
    def setUp(self): #每个用例之前都要做的操作，输入网址
        driver = self.driver
        driver.get('http://39.107.96.138:3000/signup')


    def test_register(self):
        rg = registerPage(self.driver)
        rg.input_username('helloworld')
        rg.input_pass('123456')
        rg.input_repeat_pass('123456')
        rg.input_email('')
        rg.click_register()

        text = rg.get_regiter_result(False)

        self.assertEqual(text,'信息不完整。')
