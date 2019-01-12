#一、入门
#  from selenium import webdriver

# import time   

# driver = webdriver.Chrome()

# driver.get('http://www.baidu.com') 

# baidu_input = driver.find_element_by_id('kw')
# baidu_input.send_keys("python学习")

# driver.find_element_by_id("su").click()

# time.sleep(3)

# baidu_input.clear()

# baidu_input.send_keys("hello world")

# time.sleep(2)

# result = driver.find_element_by_id('content_left')

# print(result.text)

# driver.quit()  




# 2、高级：找多个元素  ######方法未实现￥￥￥￥￥
# from selenium import webdriver

# import time 

# driver = webdriver.Chrome()

# driver.get('http://www.baidu.com') 

# navs = driver.find_elements_by_class_name('mnav')

# counter = len(navs)

# for index in range(counter):
#     print(index,navs[index].text)
#     eles = driver.find_elements_by_class_name('mnav')
#     eles[index].click()
#     driver.back()



# 2、高级：找多个元素
from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com') 

navs = driver.find_elements_by_class_name('mnav')
counter = len(navs)

for index in range(counter):
    i = index+1
    css = "#u1 > a:nth-child("+str(i)+")" 
    print("css_selector",css)
    driver.find_element_by_css_selector(css).click()
    driver.back()
