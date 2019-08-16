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


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  #引入actionchains

driver=webdriver.Chrome()

driver.get('http://39.107.96.138:3000/signin')

driver.find_element_by_xpath('//*[@id="name"]').send_keys('user1')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
driver.find_element_by_css_selector('input[type="submit"]').click()

driver.find_element_by_xpath('//*[@id="create_topic_btn"]').click()

driver.find_element_by_class_name('eicon-image').click() #点击上传图片按钮

driver.find_element_by_class_name('webuploader-element-invisible').send_keys('C:/Users/Administrator/Desktop/selenium_basic/322663.jpg')


