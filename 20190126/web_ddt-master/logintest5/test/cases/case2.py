import sys  #引入 python 标准库中的 sys.py 模块
# print (sys.path)
sys.path.append('c:\\Users\\Administrator\\Desktop\\logintest2')
import os
print (sys.path)


import unittest
from selenium import webdriver
from po.loginPage import LoginPage
import time

from ddt import ddt,data,unpack

import xlrd

def get_userInfo():  #加上这个，运行了多条用例
    wk = xlrd.open_workbook('data/user.xls') #打开这个文件
    ws = wk.sheet_by_name('userinfo') #打开这个sheet表格
    ncols = ws.ncols #获取sheet列
    nrows = ws.nrows #获取sheet行
    alldata = [] #建立个空数组
    for rowNum in range(1,nrows): #循环遍历行
        rowdata = []
        for x in range(ncols):#循环遍历列
            print("第{}列，{}行".format(x,rowNum),ws.cell_value(rowNum,x))
            rowdata.append(ws.cell_value(rowNum,x)) #获取的值一个个放到rowdata里面
            print("rowdata===",rowdata)
        alldata.append(rowdata)

    return alldata


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
    def test_login_success(self,username,password,status,asserText):
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
