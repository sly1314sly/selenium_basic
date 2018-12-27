from selenium  import webdriver  #引入一个库

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get('http://www.baidu.com')