#### 等待处理###显示等待和隐式等待

# time.sleep()这个是显示等待，又叫强制等待

# from selenium import webdriver

# from selenium.webdriver.common.by import By #引入这个by
# from selenium.webdriver.support.ui import WebDriverWait #引入等待条件
# from selenium.webdriver.support import expected_conditions as EC #根据什么条件等待



# driver = webdriver.Chrome()

# driver.implicitly_wait(10)  #隐式等待
 
# driver.get('https://outlook.live.com/owa/#')

# driver.find_element_by_css_selector('div > a.linkButtonSigninHeader:nth-child(4)').click()

# #driver.find_element(by=BY.CLASS_NAME,'topic_title').click()   #可以用by的这个方法与driver.find_element_by_class_name('topic_title').click() 是一样的

# try:
#     inputEmail = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'loginfmt'))) #### 设置最长等待时间10s，until是条件，直到这个元素加载出来，显性等待
#     # inputEmail = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_name('loginfmt'))   ##两种写法，用lambda
    
#     inputEmail.send_keys('1321312312')

# except expression as identifier:
#     print('time out...')

## driver.find_element_by_name('loginfmt').send_keys('1234455')


############################################################################################################

#### javascript

# from selenium import webdriver
# driver = webdriver.Chrome()

# #打开携程官网，将其开始时间自动改为想要的时间
# driver.get('https://www.ctrip.com/')
# start_date = '2019-08-28'

# js_script ='document.querySelector("#HD_CheckIn").value = "{}"'.format(start_date)

# print(js_script)
# driver.execute_script(js_script)


# 两种方法，要么id，要么css
#document.get……
#document.querys……

"""
// 视图滚动
document.getElementById('tables-responsive').scrollIntoView()
"""


############################################################################################################

#### 模拟手机页面
###小功能：ctrl+p 打开console，输入>cap  点击capture full size screenshot ，可以截全屏，或者手机模式下手动点击屏幕旁边的三个点找到


# from selenium import webdriver

# from selenium.webdriver.chrome.options import Options  #引入options

# mobile_emulation = {"deviceName":"iPhone X"}  #设备名
# # mobile_emulation = {"deviceName":"iPad"}   #ipad界面
# chrome_options = webdriver.ChromeOptions()

# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


# driver = webdriver.Chrome(options=chrome_options)


# driver.get('https://www.baidu.com')

############################################################################################################
#### 微博抓取页面  :八爪鱼软件可以获取

import xlwt
# from datetime import datetime

# style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
#     num_format_str='#,##0.00')
# style1 = xlwt.easyxf(num_format_str='D-MMM-YY')



# ws.write(0, 0, 1234.56, style0)
# ws.write(1, 0, datetime.now(), style1)
# ws.write(2, 0, 1)
# ws.write(555, 1, 1)
# ws.write(2, 2, xlwt.Formula("A3+B3"))

# wb.save('example.xls')



from selenium import webdriver

import time
driver = webdriver.Chrome()
driver.maximize_window() #窗口最大化
driver.implicitly_wait(30) 

driver.get('https://s.weibo.com/')


keys = 'web自动化'
wb = xlwt.Workbook()
ws = wb.add_sheet(keys)

ws.write(0,0,'用户')
ws.write(0,1,'内容')
ws.write(0,2,"时间")
ws.write(0,3,'来源')

ws.write(0,4,'收藏')
ws.write(0,5,'转发')
ws.write(0,6,'评论')
ws.write(0,7,'喜欢')


##登录
driver.find_element_by_xpath("//a[@node-type='loginBtn']").click()

driver.find_element_by_xpath("//input[@name='username']").send_keys('15256558113')
driver.find_element_by_xpath("//input[@name='password']").send_keys('*****')

driver.find_element_by_xpath('//div[6]/a').click()

time.sleep(5)

#登陆后搜索
driver.find_element_by_xpath('//input[@type="text"]').send_keys(keys)
# driver.find_element_by_xpath('//input[@type="text"]').submit() #也可以用这个方法，提交表单
driver.find_element_by_class_name('s-btn-b').click()
time.sleep(2)

#高级搜索原创的
driver.find_element_by_css_selector('[node-type="advsearch"]').click()

driver.find_element_by_css_selector('[for="radio03"]').click()

driver.find_element_by_css_selector('[node-type="OK"]').click()

rowIndex = 1
for x in range(5):
    users = driver.find_elements_by_css_selector('[action-type="feed_list_item"]') #先找每一个块
    for user in users:
        username = user.find_element_by_xpath('.//*[@class="name"]').text   #用//*代表从任意位置找的第一个，前面加个.代表的是从当前路径下去找
        content = user.find_element_by_xpath('.//*[@class="txt"]').text
        publish_date = user.find_element_by_xpath('.//*[@class="from"]/a[1]').text
        publish_source = user.find_element_by_xpath('.//*[@class="from"]/a[2]').text

        shoucang = user.find_element_by_xpath('.//*/div[@class="card-act"]/ul/li[1]/a').text
        shoucang =shoucang.split("收藏")[1] or 0  #split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
        zhuanfa = user.find_element_by_xpath('.//*/div[@class="card-act"]/ul/li[2]/a').text
        zhuanfa = zhuanfa.split("转发")[1] or 0
        pinglun = user.find_element_by_xpath('.//*/div[@class="card-act"]/ul/li[3]/a').text
        pinglun = pinglun.split("评论")[1] or 0
        xihuan = user.find_element_by_xpath('.//*/div[@class="card-act"]/ul/li[4]/a').text or 0 #拿不到文字的，只有一个数量
    
        print(username,content,publish_date,publish_source,shoucang,zhuanfa,pinglun,xihuan)
        ws.write(rowIndex,0,username)
        ws.write(rowIndex,1,content)
        ws.write(rowIndex,2,publish_date)
        ws.write(rowIndex,3,publish_source)

        ws.write(rowIndex,4,shoucang)
        ws.write(rowIndex,5,zhuanfa)
        ws.write(rowIndex,6,pinglun)
        ws.write(rowIndex,7,xihuan)

        rowIndex+=1

    # 开始点第二页
    xpath = '//*/ul[@class="s-scroll"]/li[{}]'.format(x+2)
    print(xpath)
    driver.find_element_by_class_name('pagenum').click()
    driver.find_element_by_xpath(xpath).click()


wb.save('web.xls')
driver.quit()