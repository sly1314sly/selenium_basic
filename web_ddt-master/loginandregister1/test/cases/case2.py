import sys
# print (sys.path)
sys.path.append('/Users/zyzhao/Desktop/web_ddt-master')
import os
print (sys.path)

import unittest
from selenium import webdriver
from po.loginPage import LoginPage
import common.util as Util 

import time

from ddt import ddt,data,unpack

import xlrd



def get_userInfo():
    wk = xlrd.open_workbook('data/user.xls')
    ws = wk.sheet_by_name('userinfo')
    ncols = ws.ncols
    nrows = ws.nrows
    alldata = []
    for rowNum in range(1,nrows):
        rowdata = []
        for x in range(ncols):
            print("第{}列，{}行".format(x,rowNum),ws.cell_value(rowNum,x))
            rowdata.append(ws.cell_value(rowNum,x))
            print("rowdata===",rowdata)
        alldata.append(rowdata)

    return alldata

@ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    
    def setUp(self):
        driver = self.driver
        driver.get('http://39.107.96.138:3000/signin')

    def tearDown(self):
        self.driver.delete_all_cookies()
        name = __name__
        screenShotFile = os.path.join(Util.getScreenShotsPath(),name+'.png')
        
        self.driver.save_screenshot(screenShotFile)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*get_userInfo())
    @unpack
    def test_login_1success(self,username,password,status,asserText):
        driver = self.driver
        lg = LoginPage(driver)

        lg.input_username(username)
        lg.input_password(password)
        lg.click_login_btn()
        text = lg.get_login_result(True)

        self.assertEqual(text,username,'用户名验证错误')

    @unittest.skip('skip')
    def test_login_2fail(self):
        driver = self.driver
        lg = LoginPage(driver)

        lg.input_username('1223user1')
        lg.input_password('123456')
        lg.click_login_btn()
        text = lg.get_login_result(False)

        self.assertEqual(text,'用户名或密码错误','错误提示信息验证错误')
