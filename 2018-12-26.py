#web自动化selenium其它4种查找元素的方法

from selenium import webdriver 

driver = webdriver.Chrome() 

driver.get('http://www.baidu.com')

# driver.find_element_by_class_name('s_ipt').send_keys("自动化测试")          # 如果class属性是唯一的就可以用 

# driver.find_element_by_link_text('新闻').click()        #保持外面文字是唯一的, 打开百度新闻，超链接外面的文本

driver.find_element_by_partial_link_text('新').click()       #去匹配，找到所有超链接里面带“新”字的

#  driver.find_elements_by_tag_name                      #这个很少用


# 注意：定位对象(locate elements)之后我们需要对该已定位对象进行操作 通常所有的操作与页面交互都将通过WebElement接口，常见的操作元素方法如下
# clear 清除元素的内容
# send_keys 模拟按键输入
# click 点击元素
# submit 提交表单