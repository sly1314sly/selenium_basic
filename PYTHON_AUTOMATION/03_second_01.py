### 百度获取图片验证码
# from selenium import webdriver
# import base64
# import requests

# driver = webdriver.Chrome() 
# driver.get('https://persons.shgjj.com/')

# image = driver.find_element_by_id('img1')

# image.screenshot('./01.png')

# f = open(r'./01.png', 'rb')  #打开截图

# # 参数image：图像base64编码
# img = base64.b64encode(f.read())


# ##可以在postman中先调通接口，然后把请求的数据转化成python的复制过来
# import requests

# url = "https://aip.baidubce.com/oauth/2.0/token"

# querystring = {"grant_type":"client_credentials","client_id":"1RQYVnqvNBIPoxFtzr68mWzz","client_secret":"NcQfFTMwmNyayuQiLsugfyiP05nPmnKT"}

# payload = ""
# headers = {
#     'cache-control': "no-cache",
#     'Postman-Token': "53654ba8-1fa5-419f-9cf5-d585dd302b5d"
#     }

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# # print(response.json())

# data = response.json()
# print (data['access_token'])

# access_token = data['access_token']

# url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"

# querystring = {"access_token":access_token}

# payload = {"image": img}
# headers = {
#     'Content-Type': "application/x-www-form-urlencoded",
#     'cache-control': "no-cache"
#     }

# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

# print(response.json())

# checkData = response.json()

# num = checkData['words_result'][0]['words']

# driver.find_element_by_id('imagecode1').send_keys(num)


###拖拽操作


# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains  #引入actionchains


# driver=webdriver.Chrome()

# driver.get('http://39.107.96.138:3000/signin')

# driver.find_element_by_xpath('//*[@id="name"]').send_keys('user1')
# driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
# driver.find_element_by_css_selector('input[type="submit"]').click()

# driver.find_element_by_xpath('//*[@id="create_topic_btn"]').click()

# driver.find_element_by_class_name('eicon-image').click() #点击上传图片按钮

# driver.find_element_by_class_name('webuploader-element-invisible').send_keys('C:/Users/Administrator/Desktop/selenium_basic/322663.jpg')


# #加粗操作#快捷键操作

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains  #引入actionchains
# from selenium.webdriver.common.keys import Keys
# import time

# driver=webdriver.Chrome()

# driver.get('http://39.107.96.138:3000/signin')

# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="name"]').send_keys('user1')
# driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
# driver.find_element_by_css_selector('input[type="submit"]').click()

# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="create_topic_btn"]').click() #打开发布话题

# time.sleep(2)
# content_area = driver.find_element_by_xpath('//*[@class="CodeMirror-scroll"]')  #鼠标移动到文本编辑器
# content_area.click() #点击后才能输入内容

# actions = ActionChains(driver)
# actions.move_to_element(content_area)
# actions.send_keys('hff而且')

# time.sleep(2)
# #全选
# actions.key_down(Keys.CONTROL)  
# actions.send_keys('a')
# actions.key_up(Keys.CONTROL)

# #加粗
# actions.key_down(Keys.CONTROL) 
# actions.send_keys('b')
# actions.key_up(Keys.CONTROL)

# actions.perform()


# 拖拽鼠标验证通过快捷键操作（boss直聘）

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains  #引入actionchains
# from selenium.webdriver.common.keys import Keys
# import time

# driver=webdriver.Chrome()

# driver.get('https://login.zhipin.com/?ka=header-login')

# time.sleep(2)
# span = driver.find_element_by_css_selector('form>div:nth-child(6)  div.nc_scale > span.nc_iconfont.btn_slide') #不能用id，页面一刷新，id就会变


# action = ActionChains(driver)

# action.move_to_element(span) #移动到该元素上
# action.click_and_hold() #鼠标按住不放

# action.move_by_offset(324,0) #将目标拖动到指定的位置  

# action.release() #释放按下的鼠标

# action.perform()

# #报错是因为校验了是不是自动化代码的，速度太快了


# ifame处理
# 一、安居客

# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get('https://login.anjuke.com/login/form')


# driver.switch_to_frame('iframeLoginIfm')

# driver.find_element_by_id('pwdTab').click()


# driver.find_element_by_id('pwdUserNameIpt').send_keys('12345')

# driver.find_element_by_id('pwdIpt').send_keys('sddsds')



#多嵌套的时候使用

# from selenium import webdriver
# import time

# driver = webdriver.Chrome()
# driver.get('C:/Users/Administrator/Desktop/selenium_basic/index.html')

# #找到第一个页面的iframe
# iframe1 = driver.find_element_by_tag_name('iframe')  #####

# time.sleep(2)
# #切换到下一个ifame
# driver.switch_to_frame(iframe1)  ###

# driver.switch_to_frame('iframeLoginIfm')

# driver.find_element_by_id('pwdTab').click()


# driver.find_element_by_id('pwdUserNameIpt').send_keys('12345')

# driver.find_element_by_id('pwdIpt').send_keys('sddsds')

# #切换到最原始的页面
# driver.switch_to_default_content() ###

# #页面的源代码检查一下而已
# print(driver.page_source) 




#### alert窗口处理

# from selenium import webdriver
# from selenium.webdriver.common.alert import Alert

# driver = webdriver.Chrome()

# driver.get('http://39.107.96.138:3000/signin')
# driver.find_element_by_id('name').send_keys('user1')
# driver.find_element_by_id('pass').send_keys('123456')
# driver.find_element_by_css_selector('.span-primary').click()

# driver.get('http://39.107.96.138:3000/user/user1')

# driver.find_element_by_class_name('topic_title').click()

# driver.find_element_by_css_selector('i.fa.fa-lg.fa-trash').click()

# print( Alert(driver).text)

# # 取消不删除
# Alert(driver).dismiss()
# # # 确定删除
# # Alert(driver).accept()



