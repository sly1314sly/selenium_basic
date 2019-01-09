# # web自动化selenium-写一个注册登陆来总结一下这几天的学习

# import unittest  #引入这个单元测试

# from selenium import webdriver 


# # """
# # 测试账号：
# # 用户名：user0
# # 密码：123456
# # """

# class conde(unittest.TestCase):

#     def setUp(self):
#         self.Url = 'http://39.107.96.138:3000/'
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.Url)    #打开网址

#     def test_register(self):
#         driver = self.driver
#         driver.find_element_by_css_selector('a[href="/signup"]').click()
#         driver.find_element_by_id('loginname').send_keys("zhangsanfeng")
#         driver.find_element_by_id('pass').send_keys("123456")
#         driver.find_element_by_id('re_pass').send_keys("123456")
#         driver.find_element_by_id('email').send_keys("123@163.com")
#         driver.find_element_by_css_selector('input[type="submit"]').click()
        
    
#     def test_login(self):
#         pass

#     def tearDown(self):
#         self.driver.save_screenshot('./jietu.png')    #截个图,此处会出现无论运行多少个case，都会保持为命名这个的截图，思考如何分别保留
#         self.driver.quit   #退出

# if __name__ == "__main__":
#     unittest.main()




#010-web自动化-selenium实战-如何使用action进行发帖操作

import xlrd
