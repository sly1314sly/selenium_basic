import time
import re
import pytesseract
from selenium import webdriver
from PIL import Image,ImageEnhance


driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get("http://60.174.236.99:57180/workflow-cloud")

#F:\python-jietu\screenImg.png

screenImg = "F:\python-jietu\screenImg.png"

driver.maximize_window()  #将浏览器最大化

driver.find_element_by_xpath('.//*[@id="username"]').send_keys("administrator")

time.sleep(3)

driver.find_element_by_xpath('.//*[@id="password"]').send_keys("2wsx@WSX")

time.sleep(3)


imgsrc = driver.find_element_by_id("captchaCodeImg").get_attribute('src')

#如果匹配验证码路径成功（说明有提示输入验证码），则需读取验证码！

if re.match(r'hhttp://60.174.236.99:57180/sso/captcha.htm.*', imgsrc):
	#浏览器页面截屏
	driver.get_screenshot_as_file(screenImg)
	#定位验证码位置及大小
	location = driver.find_element_by_id('captchaCodeImg').location
	size = driver.find_element_by_id('captchaCodeImg').size
	left = location['x']
	top =  location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']
	#从文件读取截图，截取验证码位置再次保存
	img = Image.open(screenImg).crop((left,top,right,bottom))
	img = img.convert('L') 			#转换模式：L | RGB
	img = ImageEnhance.Contrast(img)#增强对比度
	img = img.enhance(2.0) 			#增加饱和度
	img.save(screenImg)
	#再次读取识别验证码
	img = Image.open(screenImg)
	code = pytesseract.image_to_string(img)
	#code= pytesser.image_file_to_string(screenImg)
	driver.find_element_by_id("captchaCodeImg").send_keys(code.strip())
	print(code.strip())
 
#提交登录
driver.find_element_by_id("captchaCodeImg").click()
