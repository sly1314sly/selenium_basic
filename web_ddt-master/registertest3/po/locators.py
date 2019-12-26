#注册页面的locator

from selenium.webdriver.common.by import By

class RegisterPageLocators(object):
    USERNAME = (By.ID,'loginname')
    PASSWORD = (By.ID,'pass')
    REPASSWORD = (By.ID,"re_pass")
    EMAIL = (By.ID,'email')
    REGISTER_BTN = (By.CSS_SELECTOR,'[type="submit"]')
    SUCCESS_TEXT = (By.CSS_SELECTOR,'.alert.alert-success>strong')
    FAILED_TEXT=(By.CSS_SELECTOR,'.alert.alert-error>strong')