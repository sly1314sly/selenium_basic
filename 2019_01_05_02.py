# 四、八种定位方法
# selenium的webdriver提供了八种基本的元素定位方法，前面六种是通过元素的属性来直接定位的，后面的xpath和css定位更加灵活，需要重点掌握其中一个。
# 1.通过id定位：find_element_by_id()
# 2.通过name定位：find_element_by_name()
# 3.通过class定位：find_element_by_class_name()
# 4.通过tag定位：find_element_by_tag_name()
# 5.通过link定位：find_element_by_link_text()  
# 6.通过partial_link定位：find_element_by_partial_link_text()
# 7.通过xpath定位：find_element_by_xpath()
# 8.通过css定位：find_element_by_css_selector()

# 重点css和xpath 注：class name只能传一个值，传多个会报错
"""
> 上下级（子元素）
# id属性
. class属性
:nth-last-child(n) 第n个子元素
"""


# from selenium import webdriver

# import time   

# driver = webdriver.Chrome()

# driver.get('https://item.jd.com/100000483381.html') 

# print(driver.title)   #打印网页标题

# text = driver.find_element_by_css_selector('.price.J-p-100000483381').text  #css的选择器
# print(text)

# text2 = driver.find_element_by_css_selector('#summary-service>.hl_red').text
# print(text2)


# 五、作业：查看京东上搜也搜索手机，一页展示多少个手机，点击第一个查看


# from selenium import webdriver

# import time   

# driver = webdriver.Chrome()

# driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=91a04aab85a446d58abbb0a39947ed5f') 

# eles = driver.find_elements_by_css_selector('.gl-item>div>div.p-img>a:nth-child(1)') 

# print(len(eles))

# eles[0].click()



#查看京东上搜也搜索手机，一页展示信息分别点击查看
from selenium import webdriver

import time   

driver = webdriver.Chrome()

driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=91a04aab85a446d58abbb0a39947ed5f') 

eles = driver.find_elements_by_css_selector('.gl-item > div > div.p-img > a') 
count = len(eles)

# for index in range(count):
#     i = index+1
#     css = ".gl-item>div>div.p-img > a:nth-child("+str(i)+")" 
#     print("css_selector",css)
#     driver.find_element_by_css_selector(css).click()
#     driver.back()




for index in range(count):
    i = index+1
    driver.find_element_by_css_selector(".gl-item>div>div.p-img > a:nth-child("+str(i)+")").click()
    driver.quit()