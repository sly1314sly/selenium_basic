# 第一堂课
# 把chromedriver放到环境变量，不用每次加命令
# terminal 终端输入which python3  windows用where python
# 用open命令打开 此路径  open /Library/Frameworks/Python.framework/Versions/3.7/bin/   windows用strat

# from selenium import webdriver

# import time    #加等待时间，先引入time库

# driver = webdriver.Chrome()

# driver.get('http://www.baidu.com') 
# driver.find_element_by_id('kw').send_keys("python学习")

# driver.find_element_by_id("su").click()
# time.sleep(3)    #等待3秒
# driver.find_element_by_id("kw").clear()  #清空上次输入的内容
# driver.find_element_by_id('kw').send_keys("hello world")


from selenium import webdriver

import time    #加等待时间，先引入time库

driver = webdriver.Chrome()

driver.get('http://www.baidu.com') 

baidu_input = driver.find_element_by_id('kw')  #定义一个变量 防止后期重复的要改很多地方
baidu_input.send_keys("python学习")

driver.find_element_by_id("su").click()
time.sleep(3)    #等待3秒
baidu_input.clear()  #清空上次输入的内容
baidu_input.send_keys("hello world")

time.sleep(2)

result = driver.find_element_by_id('content_left')

print(result.text)    #打印文本

driver.quit()    #关闭浏览器，执行完毕关闭浏览器，防止占内存