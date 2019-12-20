# #Python-web数据驱动框架

#https://docs.python.org/3/library/unittest.html ##官方文档
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

    def tearDown(self):  ##运行一条用例保存一个截图
        driver = self.driver
        pngName = strftime("%Y_%b_%d_%H_%M_%S", gmtime())
        driver.save_screenshot(pngName+'.png')
        


    #@unittest.skip('跳过这条测试用例')

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



######二、装饰器：在运行测试用例时，有时需跳过或判断用例时，可以用装饰器来实现

import unittest
class test(unittest.TestCase):
    def setUp(self):
        pass
 
    @unittest.skip('跳过')
    def test_01(self):
        print("直接跳过")
    @unittest.skipIf(3>2,'当条件为TRUE跳过')
    def test_02(self):
        print("111")
    @unittest.skipUnless(3>2,'当条件为TRUE时执行测试')
    def test_03(self):
        print("222")
    #不管执行是否失败统一标记为失败
    @unittest.expectedFailure #断言的时候跳过
    def test_e(self):
        self.assertEqual(2,3)
 
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()


#######三、通过命令行运行：模块、类、或者单个测试方法 
'''
如果没有写最后的if __name__ == '__main__'方法，终端运行 python3 -m unittest +文件路径 也可以，终端运行 python3 -m unittest -v +文件路径，会把执行的方法名也显示出来

python3 -m unittest -f +文件路径：快速失败，在第一个错误或故障时停止测试运行。

运行测试模块：python -m unittest test_module1 test_module2
运行测试类：python -m unittest test_module.TestClass
运行测试方法：python -m unittest test_module.TestClass.test_method
可以在一个列表中添加需要运行的模块名、类名、方法名。
可以通过使用-v参数获取更详细的测试信息：python -m unittest -v test_module
可以通过-h参数查看命令行所有参数：python -m unittes

-b --buffer
在测试运行期间标准输出流和标准错误流被缓存。输出通过测试信息。
输出在测试失败或错误时正常回显，并添加到失败消息中。

-f, --failfast
在第一个错误或失败时停止测试运​​行。

-c --catch
Ctrl+C在测试运行期间等待当前测试结束，然后报告到目前为止的所有结果。
第二个Ctrl+C会引发KeyboardInterrupt异常。

命令行也可用于测试发现(Test Discovery)，用于运行项目中的所有测试或仅用于子集。Unittest支持简单的测试发现(Test Discovery)。为了与测试发现兼容，

所有测试文件必须是可从项目的根目录导入的模块或包（这意味着它们的文件名必须是有效的标识符）。

Test Discovery是通过TestLoader.discover()实现，也可以通过命令行实现。
基本的命令行用法：

cd project_directory #进入项目目录根目录

python -m unittest discover #执行命令

discover子命令的参数如下：

-v , --verbose 详细输出

-s , --start-directory directory 执行发现的起始目录(directory)，默认是当前目录(.)

-p, --pattern pattern 匹配测试文件的模式(pattern)，默认是test*.py

-t, --top-level-directory directory 项目(directory)的目的的根目录(默认是起始目录)

-s、-p、-t命令可以在一个命令行中联合使用。下面两个命令是等价的：

python -m unittest discover -s project_directory -p "*_test.py"

python -m unittest discover project_directory "*_test.py"

'''


# test suite(测试套件)
"""
https://blog.csdn.net/zha6476003/article/details/80493988



module.py


class baidumodule():
    def __init__(self,driver,):
        self.dr = driver #不能在类中再次导入webdriver 两边的driver等于两个窗口，直接让调用方传入driver即可
    def login(self,values):
        login_dr = self.dr
        login_dr.get("https://www.baidu.com/")
        login_dr.find_element_by_xpath("//*[@id='kw']").send_keys(values)
        login_dr.find_element_by_xpath("//*[@id='su']").click()

    def login_out(self):
        self.dr.quit()



baidu.py

# _*_ coding:utf-8 _*_
import csv,unittest #导入csv模块
from time import sleep
from selenium import webdriver
from module import baidumodule
class baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()#最大化窗口
        self.driver.implicitly_wait(10)#隐式等待
        self.search = baidumodule(self.driver) #将driver传给aidumodule这个类
        with open("file.csv","r") as name:
            self.lines = name.readlines()#以行读取整个文件
    def tearDown(self):
        self.search.login_out()

    def test_search(self):
        search = self.search
        lines = self.lines
        driver = self.driver
        search.login(lines[0])
        sleep(1)
        title = driver.title
        self.assertEqual(title,'selenium_百度搜索2')
        sleep(2)
    def test_search1(self):
        search = self.search
        lines = self.lines
        driver = self.driver
        search.login(lines[1])
        sleep(1)
        title = driver.title
        self.assertEqual(title,'selenium2_百度搜索')
        sleep(2)
    def test_search2(self):
        search = self.search
        lines = self.lines
        driver = self.driver
        search.login(lines[2])
        sleep(1)
        title = driver.title
        self.assertEqual(title,'selenium3_百度搜索')
        sleep(2)
    def test_search3(self):
        search = self.search
        lines = self.lines
        driver = self.driver
        search.login(lines[3])
        sleep(1)
        title = driver.title
        self.assertEqual(title,'webdriver_百度搜索')
        sleep(2)

class counttest(unittest.TestCase):
    def setUp(self):
        self.b = 2
        self.c = 3
    def test_add(self):
        d = self.b + self.c
        self.assertEqual(d,5)

if __name__ == "__main__":
    unittest.main()


如上我们有可能拥有n多条测试用例，我们现新增了一条test_add,我们只需要单独执行这条即可稍微改动一下if __name__ == "__main__":的代码即可

# _*_ coding:utf-8 _*_
import csv,unittest #导入csv模块
from time import sleep
from selenium import webdriver
from module import baidumodule
class baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()#最大化窗口
        self.driver.implicitly_wait(10)#隐式等待
        self.search = baidumodule(self.driver) #将driver传给aidumodule这个类
        with open("file.csv","r") as name:
            self.lines = name.readlines()#以行读取整个文件
    def tearDown(self):
        self.search.login_out()

    def test_search(self):
        search = self.search
        lines = self.lines
        driver = self.driver
        search.login(lines[0])
        sleep(1)
        title = driver.title
        self.assertEqual(title,'selenium_百度搜索2')
        sleep(2)
    def test_search1(self):
        search = self.search
        lines = self.lines
        driver = self.driver
        search.login(lines[1])
        sleep(1)
        title = driver.title
        self.assertEqual(title,'selenium2_百度搜索')
        sleep(2)
    def test_search2(self):
        search = self.search
        lines = self.lines
        driver = self.driver
        search.login(lines[2])
        sleep(1)
        title = driver.title
        self.assertEqual(title,'selenium3_百度搜索')
        sleep(2)
    def test_search3(self):
        search = self.search
        lines = self.lines
        driver = self.driver
        search.login(lines[3])
        sleep(1)
        title = driver.title
        self.assertEqual(title,'webdriver_百度搜索')
        sleep(2)

class counttest(unittest.TestCase):
    def setUp(self):
        self.b = 2
        self.c = 3
    def test_add(self):
        d = self.b + self.c
        self.assertEqual(d,5)

if __name__ == "__main__": #如果直接执行将执行以下代码，调用不执行以下代码
    # unittest.main()
    #构造测试集
    suit = unittest.TestSuite()
    suit.addTest(counttest("test_add"))#把这个类中需要执行的测试用例加进去，有多条再加即可
    #suit.addTest(counttest("test_add2"))#从上到下先后顺序
    runner = unittest.TextTestRunner()
    runner.run(suit)#运行测试用例

这样就只会执行我们指定的用例了

"""

# testloader 可以一次运行多个test

#coding=utf8 
'''
unittest提供一个TestLoader类用于自动创建一个测试集并把单个测试放入到测试集中。
TestLoader自动运行测试用例以test开头的方法的测试方法。
在多个测试用例在决定运行哪个测试用例的策略是通过内建函数对测试函数名排序决定的。
通常习惯将测试集组合在一起，以便系统一次运行所有的测试用例。
TestSuite实例添加到一个TestSuite中就像把一个TestCase实例添加到一个TestSuite中。
-----------------------------------------------------------------------------------------
suite1=module1.TheTestSuite()
suite2=module2.TheTestSuite()
alltests=unittest.TestSuite([suite1,suite2])
-----------------------------------------------------------------------------------------
可以将测试用例和测试套件的定义放在与要测试的代码相同的模块中，但将测试代码放在单独的模块中有几个好处：
1、测试模块可以从命令行独立运行。
2、测试代码可以更容易地与运输代码分开。
3、有更少的诱惑改变测试代码，以适应代码测试没有一个很好的理由。
4、测试代码的修改频率要比它测试的代码少得多。
5、测试代码可以更容易重构。
6、用C编写的模块的测试必须在单独的模块中，所以为什么不一致？
7、如果测试策略更改，则不需要更改源代码。
'''
# from __future__ import division
# from Lib.HTMLTestRunner import HTMLTestRunner
# from unittest  import TestCase,TestLoader,TestSuite
# from source.calcutor import calculatorClass
 
# class TestMul(TestCase):
#     def setUp(self):
#         pass
    
#     def test_defaultMul(self):
#         cal=calculatorClass()
#         self.assertEqual(cal.mul(),200 , "The result should be equal 200")
    
#     def test_negtiveMul(self):
#         cal=calculatorClass(-10,-25)
#         self.assertEqual(cal.mul(),250 , "The result should be equal 250")
        
#     def test_floatMul(self):
#         cal=calculatorClass(0.25,0.4)
#         self.assertEqual(cal.mul(),0.1, "The result should be equal 0.1")
    
#     def tearDown(self):
#         pass
    
# class TestDiv(TestCase):
#     def setUp(self):
#         pass
    
#     def test_defaultDiv(self):
#         cal=calculatorClass()
#         self.assertEqual(cal.mul(),0.5 , "The result should be equal 0.5")
    
#     def test_negtiveDiv(self):
#         cal=calculatorClass(-10,-25)
#         self.assertEqual(cal.mul(),0.4 , "The result should be equal 250")
        
#     def test_floatDiv(self):
#         cal=calculatorClass(0.24,0.4)
#         self.assertEqual(cal.mul(),0.6, "The result should be equal 0.1")
    
#     def tearDown(self):
#         pass
             
# def allTest():
#     ''' 创建测试集'''   
#     suite1=TestLoader().loadTestsFromTestCase(TestMul)
#     suite2=TestLoader().loadTestsFromTestCase(TestDiv)
#     alltests=TestSuite([suite1,suite2])
#     return alltests
 
# if __name__=="__main__":
#     '''创建保存测试结果的文件'''
#     html=file("..\\report.html","wb+")
#     '''调用HTMLTestRunner类生成html格式测试运行报告'''
#     runner=HTMLTestRunner(stream=html,title="Test Report",description="The state of the run testcase")
#     runner.run(allTest())
#     html.close()



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