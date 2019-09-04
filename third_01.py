# #Python-web数据驱动框架


# ###每个单元测试定义的方法名必须以test开始
# ###单元测试的顺序不是按照写的顺序执行的，是按照0-9，A-Z,a-z的顺序
# ##每个testcase运行完成后要加断言
# import unittest #引入这个单元测试

# class TestStringMethods(unittest.TestCase):  #继承这个单元测试

#     def test_upper(self):  #定义后必须以test开始才能用
#         self.assertEqual('foo'.upper(), 'FOO')  #assertEqual 断言，期望结果，判断两个值是否相等

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())  #判断是否为真
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])  #切割
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):   #assertRaises抛一个错误
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main() #unittest.main(verbosity=2)  可查看运行顺序

# """
# 这里的verbosity是一个选项,表示测试结果的信息复杂度，有三个值

# 0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
# 1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
# 2 (详细模式):测试结果会显示每个测试用例的所有相关的信息 
# 并且 你在命令行里加入不同的参数可以起到一样的效果
# 加入 –quiet 参数 等效于 verbosity=0
# 加入–verbose参数等效于 verbosity=2
# 什么都不加就是 verbosity=1  
# """

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestStringMethods(unittest.TestCase):  
    driver = webdriver.Chrome()
    driver.maximize_window()


    def test_01_login(self):
        driver = self.driver   ###注意类里面的driver
        driver.get('http://39.107.96.138:3000/signin')
        driver.find_element_by_id('name').send_keys('user1')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_css_selector('.span-primary').click()

        url=driver.current_url
        self.assertEqual(url,'http://39.107.96.138:3000/') #断言网址是否正确

        username = driver.find_element_by_css_selector('.user_name >.dark').text
        self.assertEqual(username,'user1') #断言用户名是否正确

    def test_02_fatie(self):
        driver = self.driver
        driver.get('http://39.107.96.138:3000/topic/create')

        driver.find_element_by_xpath('//*[@id="tab-value"]').click()  #点击选择框
        driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()  #下拉框选择
        driver.find_element_by_xpath('//*[@id="title"]').send_keys('helloword1') #输入主题
        content_area = driver.find_element_by_xpath('//*[@class="CodeMirror-scroll"]')  #鼠标移动到文本编辑器
        content_area.click() #点击后才能输入内容

        actions = ActionChains(driver)
        actions.move_to_element(content_area)
        actions.send_keys('hff而且')
        
        actions.perform()


    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])  #切割
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):   #assertRaises抛一个错误
    #         s.split(2)

if __name__ == '__main__':
    unittest.main(verbosity=2) 