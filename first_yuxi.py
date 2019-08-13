# 一、入门

# from selenium import webdriver    #引入selenium中webdriver这样一个库
# driver = webdriver.Chrome(executable_path='./chromedriver')    #创建一个chrome浏览器实例，加上执行的路径 。/代表当前路径(把chromedriver放到环境变量，就不用每次加命令)
# driver.get('http://www.baidu.com') #该处为具体网址，用chrome浏览器打开百度


#二、web自动化selenium通过ID,name定位元素

# driver.find_element_by_id('kw').send_keys("python学习")   #输入框输入输入关键字，通过id定位元素
# driver.find_element_by_name('wd').send_keys("python学习")   #输入框输入输入关键字 ，通过name定位元素,确保唯一
#页面中一般一个元素的id是唯一的，name是否唯一，在开发者工具页面中，点击command+f，打开查找name，是否唯一


#三、web自动化selenium通过css，xpath定位元素 线下学习css和xpath

#开发者工具，选中右键-copy-copy selector   然后按住command+f  粘贴  ，
# 如百度输入框，查找出来的是#kw ，#代表id 元素为kw，即元素为id为kw的元素
'''CSS可以通过元素的id、class、标签（input）这三个常规属性直接定位到，而这三种编写方式，在HTML中编写style的时候，可以进行标识如：
    #su 
   .class
    input
   比如：百度的登录页面
     id ===  #su                  
     class === .bg s_btn       
     标签 === input[type="submit"]  或者 input[value="百度一下"]
'''

# driver.find_element_by_css_selector('#kw').send_keys("python学习")       #css定位
# driver.find_element_by_css_selector('a[name="tj_briicon"]').click()      #css定位，上网可以查一下

#xpath定位
# //*[@id="kw"]   双斜杠表示从此页面任何一个位置开始，*去匹配，方框表示里面的属性，=是里面的值
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python学习")



#四、web自动化selenium如何自动上传文件

# driver.find_element_by_css_selector('span[class="soutu-btn"]').click() 点击
# driver.find_element_by_css_selector('input[type="file"]').send_keys('/Users/songluyao/Desktop/selenium_basic/aaa.jpg') #提供路径


#五、web自动化selenium获取网页标题-文本-添加判断

# from selenium import webdriver 
# import time   #引入时间，添加等待时间
# driver = webdriver.Chrome(executable_path='./chromedriver') 
# driver.get('http://www.baidu.com') 
# print(driver.title)

# assert "百度" in driver.title   #断言，判断百度是不是在这个里面  不在就报错，在就不会打印任何东西

# driver.find_element_by_id('kw').send_keys("自动化测试")  #百度搜索自动化测试
# driver.find_element_by_id('su').click                  #点击搜索按钮

# time.sleep(2)      #等待2秒

# rusult = driver.find_element_by_id('content_left').text   #搜索结果，调用text属性，可以拿到文本值
# print(rusult)   #打印出来
# assert "自动化测试" in rusult   #断言，有期望值



#六、web自动化selenium-Keys简介以及如何使用unittest

# from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys   #该键类提供键在键盘像enter，F1，ALT等
# driver = webdriver.Chrome() 
# driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys("自动化测试") 
# driver.find_element_by_id('kw').send_keys(Keys.ENTER)   #搜索自动化测试，按enter键搜索

'''
4）键盘事件

key_down(value, element=None) ——按下某个键盘上的键

key_up(value, element=None) ——松开某个键

send_keys(Keys.BACK_SPACE)             删除键（backspace）

send_keys( Keys. SPACE)                            空格键（space）

send_keys( Keys.TAB)                         制表键（Tab）

send_keys( Keys. ESCAPE)                  回退键（esc）

send_keys( Keys. ENTER)                    回车键（enter）

send_keys(Keys.CONTROL,’a’)         全选（ctrl+A）

send_keys(Keys.CONTROL,’c’)         复制（ctrl+C）

send_keys(Keys.CONTROL,’x’)        剪切（ctrl+X）

send_keys(Keys.CONTROL,’v’)         粘贴（ctrl+v）

send_keys(keys.F1)                             键盘F1

……

send_keys(keys.F12)                           键盘F12

 使用的时候需导入：from selenium.webdriver.common.keys import Keys
'''

#七、使用Selenium编写单元测试


# import unittest  #引入这个单元测试
# from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys   
# class BaiduSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()

#     def test_baidu_search(self):
#         driver = self.driver
#         driver.get('http://www.baidu.com')
#         driver.find_element_by_id('kw').send_keys("自动化测试") 
#         driver.find_element_by_id('kw').send_keys(Keys.ENTER)  

#     def tearDown(self):
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()



#八、web自动化selenium其它4种查找元素的方法

# from selenium import webdriver 

# driver = webdriver.Chrome() 

# driver.get('http://www.baidu.com')

# driver.find_element_by_class_name('s_ipt').send_keys("自动化测试")          # 如果class属性是唯一的就可以用 

# driver.find_element_by_link_text('新闻').click()        #保持外面文字是唯一的, 打开百度新闻，超链接外面的文本

# driver.find_element_by_partial_link_text('新').click()       #去匹配，找到所有超链接里面带“新”字的

#  driver.find_elements_by_tag_name                      #这个很少用

# 注意：定位对象(locate elements)之后我们需要对该已定位对象进行操作 通常所有的操作与页面交互都将通过WebElement接口，常见的操作元素方法如下
# clear 清除元素的内容
# send_keys 模拟按键输入
# click 点击元素
# submit 提交表单



# 九、web自动化selenium-写一个注册登陆来总结一下这几天的学习

# import unittest  #引入这个单元测试
# from selenium import webdriver 

# """
# 测试账号：
# 用户名：user0
# 密码：123456
# """

# class Conde(unittest.TestCase): #固定写法

#     def setUp(self):
#         self.Url = 'http://39.107.96.138:3000/'
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.Url)    #打开网址

#     def test_register(self):  #测试用例必须写一个test，
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
#         self.driver.quit()   #退出

# if __name__ == "__main__":
#     unittest.main()


""" 
if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
'''

'''
import unittest 

#定义测试类Test，父类为unittest.TestCase
class Test(unittest.TestCase):
# docstring for Test 

#重写父类setUp方法
def setUp(self):
    print("setUp")

#定义测试用例，以“test_”开头命名的方法
def test_test1(self):
    print("test_test1")
    self.assertEqual('1','1',msg = '1=1')

def test_test2(self):
    print('test_test2')
    self.assertEqual('1','2',msg = '1!=2')

@unittest.skip('暂时跳过test_test3的测试')
def test_test3(self):
    print('test_test2')

#重写父类tearDown方法
def tearDown(self):
    print("tearDown")

if __name__=='__main__':    
    #unittest.main()方法会搜索该模块下所有以test开头的测试用例方法
    unittest.main()

"""  
# ##############################################################
# testCase执行顺序

# 1.方法顺序
# def setUp(self): 在测试方法前执行 
# def tearDown(self): 在测试方法后执行

# --------------------- 
# class TestMethod(unittest.TestCase):
#     #每次方法之前执行
#     def setUp(self):
#         print('每次方法之前执行')

#     #每次方法之后执行
#     def tearDown(self):
#         print('每次方法之后执行')

#     def test_01(self):
#         print('测试1')

#     def test_02(self):
#         print('测试2')

# if __name__ == '__main__':
#     unittest.main()
# --------------------- 

# 执行结果：
# 每次方法之前执行
# 测试1
# 每次方法之后执行
# 每次方法之前执行
# 测试2
# 每次方法之后执行

# 2.类顺序
# @classmethod 
# def setUpClass(cls): 
# 在类之前执行
# @classmethod 
# def tearDownClass(cls): 
# 在类之后执行

# --------------------- 
# class TestMethod(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         print('类执行之前的方法')

#     @classmethod
#     def tearDownClass(cls):
#         print('类执行之后的方法')

#     #每次方法之前执行
#     def setUp(self):
#         print('每次方法之前执行')

#     #每次方法之后执行
#     def tearDown(self):
#         print('每次方法之后执行')

#     def test_01(self):
#         print('测试1')

#     def test_02(self):
#         print('测试2')

# if __name__ == '__main__':
#     unittest.main()
# --------------------- 

# 执行结果：
# 类执行之前的方法 每次方法之前执行
# 测试1
# 每次方法之后执行
# 每次方法之前执行
# 测试2
# 每次方法之后执行
# 类执行之后的方法
# ##############################################################

# 十、selenium实战，使用action进行发帖操作


# 十一、Excel文件处理—xlrd库简介

# 安装xlrd ： pip install xlrd
# github文档：https://github.com/python-excel/xlrd

# import xlrd
# book = xlrd.open_workbook('data.xls')  #打开这个文件
# print("The number of worksheets is {0}".format(book.nsheets))  #打印excel中sheet表个数
# print("Worksheet name(s): {0}".format(book.sheet_names()))  # 所有的sheet表的名字
# sh = book.sheet_by_index(0)  #第一个sheet
# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols)) #sheet的名字，多少行，多少列
# print("Cell D1 is {0}".format(sh.cell_value(rowx=0, colx=1))) #第1行，第二列的值

# for rx in range(sh.nrows): #用一个循环变了所有的值
#     print(sh.row(rx))


############################
# python 对 excel基本的操作如下：

# # -*- coding: utf-8 -*-
# import xlrd
# import xlwt
# from datetime import date,datetime
 
# def read_excel():
#   # 打开文件
#   workbook = xlrd.open_workbook(r'F:\demo.xlsx')
#   # 获取所有sheet
#   print workbook.sheet_names() # [u'sheet1', u'sheet2']
#   sheet2_name = workbook.sheet_names()[1]
 
#   # 根据sheet索引或者名称获取sheet内容
#   sheet2 = workbook.sheet_by_index(1) # sheet索引从0开始
#   sheet2 = workbook.sheet_by_name('sheet2')
 
#   # sheet的名称，行数，列数
#   print sheet2.name,sheet2.nrows,sheet2.ncols
 
#   # 获取整行和整列的值（数组）
#   rows = sheet2.row_values(3) # 获取第四行内容
#   cols = sheet2.col_values(2) # 获取第三列内容
#   print rows
#   print cols
 
#   # 获取单元格内容
#   print sheet2.cell(1,0).value.encode('utf-8')
#   print sheet2.cell_value(1,0).encode('utf-8')
#   print sheet2.row(1)[0].value.encode('utf-8')
   
#   # 获取单元格内容的数据类型
#   print sheet2.cell(1,0).ctype
 
# if __name__ == '__main__':
#   read_excel()

############################
# 十二、查找多个元素

#页面所有手机价格找到打印出来
# from selenium import webdriver
# import time   
# driver = webdriver.Chrome()
# driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=91a04aab85a446d58abbb0a39947ed5f') 
# eles = driver.find_elements_by_css_selector('li.gl-item .p-price') 
# for index in range(len(eles)):
#     print(eles[index].text)

#十三、excel文件处理——写入到文件
