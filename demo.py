from selenium import webdriver    #引入selenium中webdriver这样一个库

driver = webdriver.Chrome(executable_path='./chromedriver')    #创建一个chrome浏览器实例，加上执行的路径

driver.get('http://www.baidu.com') #该处为具体网址，用chrome浏览器打开百度


     #web自动化selenium通过ID,name定位元素
# driver.find_element_by_id('kw').send_keys("python学习")   #输入框输入输入关键字，通过id定位元素

# driver.find_element_by_name('wd').send_keys("python学习")   #输入框输入输入关键字 ，通过name定位元素

      #页面中一般一个元素的id是唯一的，name是否唯一，在开发者工具页面中，点击command+f，打开查找name，是否唯一


      #web自动化selenium通过css，xpath定位元素 线下学习css和xpath
      #开发者工具，选中右键-copy-copy selector   然后按住command+f  粘贴  ，
      # 如百度输入框，查找出来的是#kw ，#代表id 元素为kw，即元素为id为kw的元素

# driver.find_element_by_css_selector('#kw').send_keys("python学习")

# driver.find_element_by_css_selector('a[name="tj_briicon"]').click()  #css定位，去参考

      #xpath定位
      #//*[@id="kw"]   双斜杠表示从此页面任何一个位置开始，*去匹配，方框表示里面的属性，=是里面的值
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python学习")


#web自动化selenium如何自动上传文件

# driver.find_element_by_css_selector('span[class="soutu-btn"]').click()
# driver.find_element_by_css_selector('input[type="file"]').send_keys('/Users/songluyao/Desktop/selenium_basic/aaa.jpg')