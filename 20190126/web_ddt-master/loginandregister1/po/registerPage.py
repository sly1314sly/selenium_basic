
from po.locators import RegisterPageLocators

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class registerPage(BasePage):

    def input_username(self,username):
        ele = self.driver.find_element(*RegisterPageLocators.USERNAME)
        ele.clear()
        ele.send_keys(username)

    def input_pass(self,password):
        ele = self.driver.find_element(*RegisterPageLocators.PASSWORD)
        ele.clear()
        ele.send_keys(password)

    def input_repeat_pass(self, repeat_pass):
        ele = self.driver.find_element(*RegisterPageLocators.REPASSWORD)
        ele.clear()
        ele.send_keys(repeat_pass)
    
    def input_email(self,email):
        ele = self.driver.find_element(*RegisterPageLocators.EMAIL)
        ele.clear()
        ele.send_keys(email)
    
    def click_register(self):
        ele = self.driver.find_element(*RegisterPageLocators.REGISTER_BTN)
        ele.click()

    def get_regiter_result(self,status):
        if expect_status == True:
            login_success_message_text = self.driver.find_element(*RegisterPageLocators.SUCCESS_TEXT).text
            return login_success_message_text
        else:
            login_fail_message_text = self.driver.find_element(*RegisterPageLocators.FAILED_TEXT).text
            return login_fail_message_text