# -*- coding:UTF-8 -*-

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import choice
import re
#import pickle

browser = webdriver.Chrome()  # 打开谷歌浏览器
wait = ui.WebDriverWait(browser,10) # 设定最长等待加载时间为10秒

browser.get("http://s.weibo.com/") #打开微博搜索的地址

def login(username,password):

    wait.until(lambda browser: browser.find_element_by_xpath("//a[@node-type='loginBtn']"))  #找到左上角登录按钮
    browser.find_element_by_xpath("//a[@node-type='loginBtn']").click()  #点击登录按钮
    
    wait.until(lambda browser: browser.find_element_by_xpath("//input[@name='username']"))  #等待登录页面出现
    user = browser.find_element_by_xpath("//input[@name='username']")
    user.clear()
    user.send_keys(username)   #输入用户名
    psw = browser.find_element_by_xpath("//input[@name='password']")
    psw.clear()
    psw.send_keys(password)  #输入密码
    browser.find_element_by_xpath("//div[6]/a/span").click()   #点击“登录”

##输入关键词搜索
def search(searchWord):
    
    wait.until(lambda browser: browser.find_element_by_class_name("gn_name"))  #等待用户名出现，确认登录成功
    
    inputBtn = browser.find_element_by_class_name("searchInp_form") #找到搜索框
    inputBtn.clear()
    inputBtn.send_keys(searchWord.strip().decode("gbk"))  #输入搜索关键词

    browser.find_element_by_class_name('searchBtn').click()  #点击“搜索”
    
    #wait.until(lambda browser: browser.find_element_by_class_name("search_num"))

#texts = browser.find_elements_by_xpath("//dl[@class='feed_list W_linecolor ']/dd[@class='content']/p[@node-type='feed_list_content']/em")

##解析页面
def gettext():
    content =[]  #定义一个list，用来装一条条的微博
    wait.until(lambda browser: browser.find_element_by_class_name("search_page_M"))  #等待翻页的元素出现
    texts = browser.find_elements_by_xpath("//dl[@action-type='feed_list_item']/dd[@class='content']/p[@node-type='feed_list_content']/em")  #获取微博内容
    #print len(texts)
    for n in texts:
        try:
            highpoints = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
            mytext =  highpoints.sub(u'',n.text)
            ##emojiToDie 顾名思义，是为了解决微博文本内容里的emoji图像而建立的一个正则表达式，我为什么这么恨emoji呢，因为你在往数据库里存，在解析它的时候，都会报错，所以干脆给它过滤掉
            print(mytext.encode("gbk"))
            content.append(mytext.encode("utf-8"))##把每一条微博加到容器里
    return content

##翻页 
def nextPage():
    #wait.until(lambda browser: browser.find_element_by_class_name("search_page_M")) #等翻页的元素出现
    if browser.find_elements_by_xpath("//ul[@class='search_page_M']") != None:
        nums = len(browser.find_elements_by_xpath("//ul[@class='search_page_M']/li"))
        #browser.execute_script("window.scrollTo(0, 7100)")
        pg = browser.find_element_by_xpath("//ul[@class='search_page_M']/li[%d]/a" %nums) #.text.encode("gbk")#找到“下一页”
        y = pg.location['y']+100#找到“下一页”在页面的高度
        print(y) 
        browser.execute_script('window.scrollTo(0, {0})'.format(y))    #滚动到“下一页”所在的行，必须让“下一页”出现在画面里，才能进行点击，这一点是血的教训 
        ActionChains(browser).move_to_element(pg).click(pg).perform()#鼠标放到下一页上，点击，为啥不直接用click呢，因为会报错，说元素not clickable，泪的教训
# 5、组合
# 所有的功能都完成了，接下来要让它能循环地去抓取，我们还需要写个main()函数
def main():
    login()
    search("guanjianzi")
    text =[]
    for i in range(0,10):
        text=text +gettext()
        sleep(choice([1,2,3,4])) ##随机等待1或2或3或4秒，别抓太勤，微博会怀疑你是机器人的
        nextPage()         
    print(len(text))
    
main()