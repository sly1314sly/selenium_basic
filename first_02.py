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

# from selenium import webdriver
# import time
# driver = webdriver.Chrome()

# #打开手机列表界面
# driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=91a04aab85a446d58abbb0a39947ed5f') 
# print("打开首页之后，浏览器tab页面个数",len(driver.window_handles))  #driver.window_handles：获取所有窗口句柄

# #查找页面上的手机列表
# eles = driver.find_elements_by_css_selector('.gl-item>div>div.p-img>a:nth-child(1)') 
# print(len(eles))
# counter = len(eles) 

# for i in range(counter):
#     eles[i].click()
#     allwindows = driver.window_handles  #获取所有的窗口
#     driver.switch_to.window(allwindows[1])    #切换到第二个新打开的窗口
#     time.sleep(2)
#     text = driver.find_element_by_css_selector('span.p-price>span.price').text  #定位到价格
#     print(text)
#     driver.close() #关闭当前标签页，即第二个窗口
#     driver.switch_to.window(allwindows[0])    #切换到第一个窗口

#     time.sleep(2) 


 ## 如何用xpath定位元素
 #  //*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img
#其中//*[@id="J_goodsList"]这一段是指在根元素下查找任意id为J_goodsList的元素，后面的路径必须按照源码的层级依次往下写。

#参考资料网站
#https://www.w3school.com.cn/xpath/xpath_syntax.asp  
#菜鸟教程css
#https://selenium-python.readthedocs.io/api.html

## 登陆此网站，发布一个话题
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  #引入actionchains

driver=webdriver.Chrome()

driver.get('http://39.107.96.138:3000/signin')   # 账号密码user1 123456

driver.find_element_by_xpath('//*[@id="name"]').send_keys('user1')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
driver.find_element_by_css_selector('input[type="submit"]').click()

driver.find_element_by_xpath('//*[@id="create_topic_btn"]').click() #打开发布话题
driver.find_element_by_xpath('//*[@id="tab-value"]').click()  #点击选择框
driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()  #下拉框选择
driver.find_element_by_xpath('//*[@id="title"]').send_keys('helloword1') #输入主题

content_area = driver.find_element_by_xpath('//*[@class="CodeMirror-scroll"]')  #鼠标移动到文本编辑器
content_area.click() #点击后才能输入内容
actions = ActionChains(driver)
actions.move_to_element(content_area)
actions.send_keys('hff而且')

actions.perform()

driver.find_element_by_xpath('//*[@type="submit"]').click() #提交

'''
下面是一些常用的模拟鼠标的操作
鼠标单击     click(on_element=None) 
- 如果参数不写，那么点击的是当前鼠标位置
- 如果参数写定位到的元素对象element，那就是点这个元素

鼠标单击并且按住不放     click_and_hold(on_element=None) 
- 如果参数不写，那么点的是当前鼠标位置
- 如果参数写定位到的元素对象element，那就是点这个元素

右击     context_click(on_element=None)
- 如果参数不写，那么点的是当前鼠标位置
- 如果参数写定位到的元素对象element，那就是点这个元素

双击     double_click(on_element=None)
- 如果参数不写，那么点的是当前鼠标位置
- 如果参数写定位到的元素对象element，那就是点这个元素

拖拽     drag_and_drop(source, target)
- source: 按住鼠标的元素位置
- target: 松开鼠标的元素位置

将目标拖动到指定的位置     drag_and_drop_by_offset(source, xoffset, yoffset)
- source: 按住鼠标的元素位置
- xoffset: X 轴的偏移量
- yoffset: Y 轴的偏移量

按住某个键，使用这个方法可以方便的实现某些快捷键,     key_down(value, element=None)
                         比如下面按下Ctrl+c键     ActionsChains(browser).key_down(Keys.CONTROL).send_keys('c').perform()
- value: 要发送的修饰符键。值在“Keys”类中定义。
- element: 定位的元素
如果element参数不写就是当前鼠标的位置

松开某个键，可以配合上面的方法实现按下Ctrl+c并且释放     key_up(value, element=None)
                                                 ActionsChains(browser).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

指定鼠标移动到某一个位置，需要给出两个坐标位置     move_by_offset(xoffset, yoffset)
- xoffset: X轴 作为一个正整数或负整数移动到x偏移量
- yoffset: Y轴 偏移，作为正整数或负整数。

将鼠标移动到指定的某个元素的位置     move_to_element(to_element)
- to_element: 定位需要悬停的元素

移动鼠标到某个元素位置的偏移位置     move_to_element_with_offset(to_element, xoffset, yoffset)
- to_element: 定位需要悬停的元素
- xoffset: X 轴偏移量
- yoffset: Y 轴偏移量

将之前的一系列的ActionChains执行     perform()

释放按下的鼠标     release(on_element=None)
- 如果参数不写，那么是当前鼠标位置
- 如果参数写定位到的元素对象element，那就是这个元素.

向某个元素位置输入值     send_keys(*keys_to_send)
要发送的按键。修饰符键常数可以在“Keys”类。

向指定的元素输入数据     send_keys_to_element(element, *keys_to_send)
- element: 定位的元素
- keys_to_send: 要发送的按键。修饰符键常数可以在“Keys”类。

'''

# 遇到验证码一般操作：
# 1、让开发把验证码规避掉，在测试环境设置一个万能码
# 2、人工智能的图像识别，一般不一定每一个都能识别成功，百度或阿里的图像识别

#selenium做网页自动化，如何下载文件