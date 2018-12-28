#web自动化selenium-Keys简介以及如何使用unittest

from selenium import webdriver 

from selenium.webdriver.common.keys import Keys   #该键类提供键在键盘像RETURN，F1，ALT等

driver = webdriver.Chrome() 

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys("自动化测试") 

driver.find_element_by_id('kw').send_keys(Keys.ENTER)   #搜索自动化测试，按enter键搜索







# #使用Selenium编写单元测试

# import unittest  #引入这个单元测试

# from selenium import webdriver 

# from selenium.webdriver.common.keys import Keys   #该键类提供键在键盘像RETURN，F1，ALT等

# class BaiduSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()

#     def test_baidu_search(self):
#         driver = self.driver
#         driver.get('http://www.baidu.com')
#         driver.find_element_by_id('kw').send_keys("自动化测试") 
#         driver.find_element_by_id('kw').send_keys(Keys.ENTER)   #搜索自动化测试，按enter键搜索

#     def tearDown(self):
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()
