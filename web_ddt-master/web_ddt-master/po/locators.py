from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'[type="submit"]')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass

class RegisterPageLocators(object):
    USERNAME = (By.ID,'loginname')
    PASSWORD = (By.ID,'pass')
    REPASSWORD = (By.ID,"re_pass")
    EMAIL = (By.ID,'email')
    REGISTER_BTN = (By.CSS_SELECTOR,'[type="submit"]')
    SUCCESS_TEXT = (By.CSS_SELECTOR,'.alert.alert-success>strong')
    FAILED_TEXT=(By.CSS_SELECTOR,'.alert.alert-error>strong')