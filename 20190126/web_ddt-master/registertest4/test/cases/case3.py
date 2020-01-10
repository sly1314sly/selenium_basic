##注册用例

   
import unittest
from selenium import webdriver
from po.registerPage import registerPage
import os
import time

from ddt import ddt, data, file_data

@ddt
class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    
    def setUp(self): #每个用例之前都要做的操作，输入网址
        driver = self.driver
        driver.get('http://39.107.96.138:3000/signup')

    @file_data('C:/Users/Administrator/Desktop/registertest4/data/case3.json')  #json的路径
    def test_register(self,username,password,repass,email,status,message):
        rg = registerPage(self.driver)
        rg.input_username(username)
        rg.input_pass(password)
        rg.input_repeat_pass(repass)
        rg.input_email(email)
        rg.click_register()

        text = rg.get_regiter_result(status)

        self.assertEqual(text,message)
