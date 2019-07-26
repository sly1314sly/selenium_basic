# 第一堂课

# 一：chrome开发工具使用说明
# 把chromedriver放到环境变量，不用每次加命令
# terminal 终端输入which python3（mac电脑）  windows电脑用where python
# 用open命令打开 此路径  open /Library/Frameworks/Python.framework/Versions/3.7/bin/   windows用start


#二、用id元素定位
# from selenium import webdriver

# import time    #加等待时间，先引入time库

# driver = webdriver.Chrome()

# driver.get('http://www.baidu.com') 
# driver.find_element_by_id('kw').send_keys("python学习")

# driver.find_element_by_id("su").click()
# time.sleep(3)    #等待3秒
# driver.find_element_by_id("kw").clear()  #清空上次输入的内容
# driver.find_element_by_id('kw').send_keys("hello world")

#定义了一个变量 防止后期代码修改改很多地方
# from selenium import webdriver

# import time    #加等待时间，先引入time库

# driver = webdriver.Chrome()

# driver.get('http://www.baidu.com') 

# baidu_input = driver.find_element_by_id('kw')  #定义一个变量 防止后期重复的要改很多地方

# baidu_input.send_keys("python学习")

# driver.find_element_by_id("su").click()

# time.sleep(3)    #等待3秒

# baidu_input.clear()  #清空上次输入的内容

# baidu_input.send_keys("hello world")

# time.sleep(2)

# result = driver.find_element_by_id('content_left')

# print(result.text)    #打印文本

# driver.quit()    #关闭浏览器，执行完毕关闭浏览器，防止占内存



# 三、用name元素定位
# 1、普通
# from selenium import webdriver

# import time    #加等待时间，先引入time库

# driver = webdriver.Chrome()

# driver.get('http://www.baidu.com') 

# driver.find_element_by_name('tj_trnews').click()

# driver.quit()   



# 2、高级：找多个元素
from selenium import webdriver

import time    #加等待时间，先引入time库

driver = webdriver.Chrome()

driver.get('http://www.baidu.com') 


# a、未实现方法
# navs = driver.find_elements_by_class_name('mnav')   #找多个元素,返回所有元素，去写个循环，拿元素
# for index in range(len(navs)):
#     print(index,navs[index].text)
#     navs[index].click()
#     driver.back()  #倒退  
#     driver.get('http://www.baidu.com')    #selenium的每次打开页面都会新创一个session id ，driver每次打开的是不一样 所以会报错

# b、正确方法
navs = driver.find_elements_by_class_name('mnav')  #find_element与find_elements,一个是查找一个元素，一个是查找多个元素
counter = len(navs)

for index in range(counter):
    i = index+1
    css = "#u1 > a:nth-child("+str(i)+")"     #思路：根据选择器查找，css或者xpath，通过添加索引值，定位不同元素，把索引值放在选择器里面
    print("css_selector",css)
    driver.find_element_by_css_selector(css).click()
    driver.back()  #倒退 


    # driver.back()  #倒退  
    # driver.refresh #刷新
    # driver.forward #前进
    # driver.maximize_window #最大化窗口
    # driver.minimize_window #最小化窗口