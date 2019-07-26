from selenium import webdriver  
import time

driver = webdriver.Chrome()  
driver.get('http://dev.console.jobsaas.com')

time.sleep(2) 

driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/form/div[2]/div[1]/div/div[1]/input').send_keys("15256558113")
driver.find_element_by_css_selector('input[type="password"]').send_keys("558113")
