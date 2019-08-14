from selenium import webdriver  
import requests,base64
import time

driver = webdriver.Chrome()  
driver.get('http://dev.console.jobsaas.com')

time.sleep(2) 

driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/form/div[2]/div[1]/div/div[1]/input').send_keys("15256558113")
driver.find_element_by_css_selector('input[type="password"]').send_keys("558113")

image_ele = driver.find_element_by_css_selector('div.loginVerImg.fr > img') #找到图片验证码位置

image_ele.screenshot('./image.png') #把图片截图保存下来


#获取百度APK的token。client_id 为官网获取的AK，client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=gZcF5SoXusyYZbmdXb6x8YFq&client_secret=q5ylwgyYulmxd4boMa1qLDkAMDIAy8Eu'
res= requests.get(host) #用requeest发用get请求
r =res.json()
print(r)

access_token = r['access_token'] #获取json里面的token
print(access_token)

# access_token = '#####调用鉴权接口获取的token#####'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token='+access_token
# 二进制方式打开图文件
f = open(r'./image.png', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
imageres = requests.post(url, data=params) #用这个方法上传上去，上传url和数据
image_json = imageres.json() #返回结果
print(imageres.json())

image_num = image_json['words_result'][0]['words'] #获取图片验证码上的内容
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/form/div[2]/div[3]/div/div[1]/input').send_keys(image_num) #输入图片验证码

