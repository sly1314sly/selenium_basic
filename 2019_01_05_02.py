# 四、八种定位方法
# selenium的webdriver提供了八种基本的元素定位方法，前面六种是通过元素的属性来直接定位的，后面的xpath和css定位更加灵活，需要重点掌握其中一个。
# 1.通过id定位：find_element_by_id()               #要保证页面值是唯一的
# 2.通过name定位：find_element_by_name()           #要保证页面值是唯一的
# 3.通过class定位：find_element_by_class_name()    #要保证页面值是唯一的，如果class name有多个值，传多个会报错，只能传一个值
# 4.通过tag定位：find_element_by_tag_name()        #按照标签名定位元素，几乎不会用到
# 5.通过link定位：find_element_by_link_text()      #要保证页面值是唯一的，针对超链接文件定位
# 6.通过partial_link定位：find_element_by_partial_link_text()  #要保证页面值是唯一的，针对超链接文件定位，可以模糊匹配
# 7.通过xpath定位：find_element_by_xpath()
# 8.通过css定位：find_element_by_css_selector()

# By.id(id)、By.xpath(xpath);使用最多的定位方式
# By.linkText(linkText)，By.partialLinkText(linkText)  a标签的不二之选
# By.tagName(name) 特别好用的定位方式
# By.className(className)可以解决很大的问题
# By.cssSelector(selector) 超级无敌好用


# 重点css和xpath 注：class name只能传一个值，传多个会报错
"""
> 上下级（子元素）
# id属性
. class属性
:nth-last-child(n) 第n个子元素
"""
# 如何用css定位元素
# 1、简单的用法
# 选择到元素上，选中右键-copy-copy selector   然后按住command+f  粘贴
# 2、> 上下级（子元素）；.代表class，如'.price.J-p-100000483381'；#表示id
    

# from selenium import webdriver
# import time   
# driver = webdriver.Chrome()
# driver.get('https://item.jd.com/100000483381.html') 
# print(driver.title)   #打印网页标题
# text = driver.find_element_by_css_selector('.price.J-p-100000483381').text  #css的选择器,打印商品价格
# print(text)
# text2 = driver.find_element_by_css_selector('#summary-service>.hl_red').text #找到京东
# print(text2)



# 五、作业：查看京东上搜也搜索手机，一页展示多少个手机，点击第一个查看
# from selenium import webdriver
# import time   
# driver = webdriver.Chrome()
# driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=91a04aab85a446d58abbb0a39947ed5f') 
# eles = driver.find_elements_by_css_selector('.gl-item>div>div.p-img>a:nth-child(1)') 
# print(type(eles))
# print(len(eles))
# eles[0].click()



# # #查看京东上搜也搜索手机，一页展示信息分别点击查看*********************************************

# 方法一：未能实现， 打开一个页面，点击链接跳入到新的页面，需要做切换页面的操作，才能对第二个页面进行操作
# from selenium import webdriver
# import time   
# driver = webdriver.Chrome()
# driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=91a04aab85a446d58abbb0a39947ed5f') 
# eles = driver.find_elements_by_css_selector('.gl-item > div > div.p-img > a') 
# count = len(eles)
# for index in range(count):
#     i = index+1
#     css = ".gl-item>div>div.p-img > a:nth-child("+str(i)+")" 
#     print("css_selector",css)
#     driver.find_element_by_css_selector(css).click()
#     driver.back()



# # 方法二：正确方法

from selenium import webdriver
import time
driver = webdriver.Chrome()

#打开手机列表界面
driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=91a04aab85a446d58abbb0a39947ed5f') 
print("打开首页之后，浏览器tab页面个数",len(driver.window_handles))  #driver.window_handles：获取所有窗口句柄

#查找页面上的手机列表
eles = driver.find_elements_by_css_selector('.gl-item>div>div.p-img>a:nth-child(1)') 
print(len(eles))
counter = len(eles) 

for i in range(counter):
    eles[i].click()
    allwindows = driver.window_handles  #获取所有的窗口
    driver.switch_to.window(allwindows[1])    #切换到第二个新打开的窗口
    time.sleep(2)
    text = driver.find_element_by_css_selector('span.p-price>span.price').text  #定位到价格
    print(text)
    driver.close() #关闭当前标签页，即第二个窗口
    driver.switch_to.window(allwindows[0])    #切换到第一个窗口窗口

    time.sleep(2) 