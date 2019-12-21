
from elements import BasePageElement
from selenium.webdriver.common.by import By


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = '.user_name >.dark'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver




class LoginPage(BasePage):
    
    def __init__(self,driver,username,password):
        self.driver = driver
        self.driver = driver
        self.username = username
        self.password = password

    def login(self):
        """
        用户登录操作
        """
        self.driver.get('http://39.107.96.138:3000/signin')
        self.driver.find_element_by_id('name').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_css_selector('.span-primary').click()


    def get_login_name(self):
        """
        登录成功后，获取用户名，return str
        """
        # username = self.driver.find_element_by_css_selector('.user_name >.dark').text
        locator = (By.CSS_SELECTOR,'.user_name >.dark')
        text = BasePageElement(self,driver).get_Text
        return text