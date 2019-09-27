# #Python-web数据驱动框架


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



# ###每个单元测试定义的方法名必须以test开始
# ###单元测试的顺序不是按照写的顺序执行的，是按照0-9，A-Z,a-z的顺序
# ##每个testcase运行完成后要加断言
###执行顺序：setUpClass-->setUp-->testcase-->tearDown-->tearDownClass


import unittest
from time import gmtime,strftime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestStringMethods(unittest.TestCase):  
    
    @classmethod
    def setUpClass(cls): #是class的一个方法，在所有的test前被调用
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()



##setup主要是进行测试前的初始化工作,在一个类类里面最先被调用的函数
    def setUp(self): 
        pass

    def tearDown(self):  ##
        driver = self.driver
        pngName = strftime("%Y_%b_%d_%H_%M_%S", gmtime())
        driver.save_screenshot(pngName+'.png')
        



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

    @classmethod  #运行完成后全部退出
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2) 




'''
注意：
1.什么是setUp()和tearDown()函数？
　　♦ setUp()函数是在众多函数或者说是在一个类类里面最先被调用的函数，
而且每执行完一个函数都要从setUp()调用开始后再执行下一个函数，有几个函数就调用他几次，与位置无关，随便放在那里都是他先被调用。
　　♦ tearDown(）函数是在众多函数执行完后他才被执行，意思就是不管这个类里面有多少函数，
他总是最后一个被执行的，与位置无关，放在那里都行，最后不管测试函数是否执行成功都执行tearDown()方法；
如果setUp()方法失败，则认为这个测试项目失败，不会执行测试函数也不执行tearDown()方法。

2.为什么我们要用setUp()和tearDown()函数？
　　♦ 我们利用这一特性在自动化中setup主要是进行测试前的初始化工作，比如在接口测试前面做一些前置的参数赋值，数据库操作等等 teardown是测试后的清除工作，比如参数还原或销毁，数据库的还原恢复等
'''

# from selenium import webdriver
# import unittest#第一步引入一个unittest
# import time
# class Buy_Broject_Establish(unittest.TestCase):#第二步创建继承一个unittest.TestCase的类
#     def setUp(self):#第三步定义一个setup，放一些准备的工作，或者准备一些测试数据。
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()#放大浏览器
#         self.driver.get("http://10.20.24.45:8080/amcs/login.htm")
#         print(self.driver.title)#获取标题头并打印出来
#         print(self.driver.current_url)#获取当前页面的url
#         time.sleep(5)
#     def test_001(self):#进入登录页面
#         self.driver.find_element_by_id('account_content').send_keys("admin")#输入账号
#         self.driver.find_element_by_id('account_pass').send_keys("1")#输入密码
#         self.driver.find_element_by_id('submitBtn').click()#点击登录
#         time.sleep(2)
#         print(u'进入首页')
#     def test_002(self):#进入收购项目管理首页
#         self.driver.find_element_by_xpath('//*[@id="J-h-menu-body"]/ul/li[3]/a').click()#进入项目管理
#         self.driver.find_element_by_xpath('//*[@id="J-h-menu-body"]/ul/li[3]/ul/li[1]/a/span').click()#进入收购项目管理
#         self.driver.implicitly_wait(5)#隐试等待
#         self.driver.switch_to.frame('mainFrame_assetPacketManagePro')#进入一个iframe。
#         time.sleep(10)
#         print('进入收购项目管理')
#     def tearDown(self):#第三步：定义一个tearDown，当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
#             self.driver.quit()
# if __name__ == '__main__':#如果其他的类调用的这个类的时候他就会自动忽略掉这个函数，他是为了测试自身的类用的
#     unittest.main()#启动程序

###执行顺序如下：setUp---test_001---setUp---test_002---tearDown