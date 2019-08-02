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

import unittest  #引入这个单元测试
from selenium import webdriver 

# """
# 测试账号：
# 用户名：user0
# 密码：123456
# """

class Conde(unittest.TestCase):

    def setUp(self):
        self.Url = 'http://39.107.96.138:3000/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)    #打开网址

    def test_register(self):  #测试用例必须写一个test，
        driver = self.driver
        driver.find_element_by_css_selector('a[href="/signup"]').click()
        driver.find_element_by_id('loginname').send_keys("zhangsanfeng")
        driver.find_element_by_id('pass').send_keys("123456")
        driver.find_element_by_id('re_pass').send_keys("123456")
        driver.find_element_by_id('email').send_keys("123@163.com")
        driver.find_element_by_css_selector('input[type="submit"]').click()
        
    
    def test_login(self):
        pass

    def tearDown(self):
        self.driver.save_screenshot('./jietu.png')    #截个图,此处会出现无论运行多少个case，都会保持为命名这个的截图，思考如何分别保留
        self.driver.quit()   #退出

if __name__ == "__main__":
    unittest.main()

'''
if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
'''

# 十、selenium实战，使用action进行发帖操作
