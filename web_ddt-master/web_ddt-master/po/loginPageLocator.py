
from selenium.webdriver.common.by import By
class LoginPageLocator(object):
    USERNAME=(By.ID,'name')
    PASSWORD=(By.ID,"pass")
    LOGIN_BTN=(By.CSS_SELECTOR,'[type="submit"]')
    SUCCESS_TEXT=(By.CSS_SELECTOR,'.user_name>a.dark')
    FAILED_TEXT=(By.CSS_SELECTOR,'.alert.alert-error > strong')
