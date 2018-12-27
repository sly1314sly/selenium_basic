#web自动化selenium获取网页标题-文本-添加判断

from selenium import webdriver 

import time   #引入时间，添加等待时间

driver = webdriver.Chrome(executable_path='./chromedriver') 

driver.get('http://www.baidu.com') 

print(driver.title)

assert "百度" in driver.title   #断言，判断百度是不是在这个里面  不在就报错，在就不会打印任何东西

# # assert "谷歌" in driver.title   #断言，判断百度是不是在这个里面  不在就报错，在就不会打印任何东西

driver.find_element_by_id('kw').send_keys("自动化测试")  #百度搜索自动化测试
driver.find_element_by_id('su').click                  #点击搜索按钮

time.sleep(2)      #等待2秒

rusult = driver.find_element_by_id('content_left').text   #搜索结果，调用text属性，可以拿到文本值
print(rusult)   #打印出来

assert "自动化测试" in rusult   #断言，有期望值

