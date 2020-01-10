
'''
1、每个单元测试定义的方法名必须以test开始
2、单元测试的顺序不是按照写的顺序执行的，是按照0-9，A-Z,a-z的顺序
3、unittest 执行时序
  setUpClass            所有的testcase 执行之前运行
  setUp                 每个testcase执行之前运行
  tearDown              每个testcase执行之后运行
  tearDownClass         所有的testcase执行之后运行
'''



import unittest
from time import gmtime,strftime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestStringMethods3(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #是class的一个方法，在所有的testcase前被调用
        print('setUpClass')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()


    def setUp(self): #每个testcase执行之前要做的操作
        pass

    def tearDown(self):  ##每个testcase执行之后要做的操作，此处是运行一条用例保存一个截图。
        driver = self.driver
        pngName = strftime("%Y_%b_%d_%H_%M_%S", gmtime())   #用每次运行的日期不一样，以日期命名截图，就不会覆盖
        driver.save_screenshot(pngName+'.png')    
            

    def test_01_login(self):
        driver = self.driver   ###注意类里面的driver
        driver.get('http://39.107.96.138:3000/signin')
        driver.find_element_by_id('name').send_keys('testuser1')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_css_selector('.span-primary').click()

        url=driver.current_url
        self.assertEqual(url,'http://39.107.96.138:3000/') #断言网址是否正确

        username = driver.find_element_by_css_selector('.user_name >.dark').text
        self.assertEqual(username,'testuser1') #断言用户名是否正确

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


    @classmethod  #运行完成后全部退出，所有的testcase执行之后运行
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)