
from selenium.webdriver.common.by import By
from po.loginPageLocator import LoginPageLocator

class LoginPage(object):


    def __init__(self,driver):
        self.driver = driver

    def input_username(self,username):
        ele = self.driver.find_element(*LoginPageLocator.USERNAME)
        ele.clear()
        ele.send_keys(username)

    def input_password(self,password):
        ele = self.driver.find_element(*LoginPageLocator.PASSWORD)
        ele.clear()
        ele.send_keys(password)

    def click_login_btn(self):
        ele = self.driver.find_element(*LoginPageLocator.LOGIN_BTN)
        ele.click()
    

    def get_login_result(self,expect_status):
        if expect_status == True:
            login_success_message_text = self.driver.find_element(*LoginPageLocator.SUCCESS_TEXT).text
            return login_success_message_text
        else:
            login_fail_message_text = self.driver.find_element(*LoginPageLocator.FAILED_TEXT).text
            return login_fail_message_text