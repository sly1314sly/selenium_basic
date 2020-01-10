
from elements import BasePageElement
from selenium.webdriver.common.by import By


class SearchTextElement(BasePageElement):
    
    locator = '.user_name >.dark'


class BasePage(object):
    

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
        locator1 = (By.ID,'name')
        BasePageElement(self.driver).input_info(locator1,self.username)
        locator2 = (By.ID,'pass')
        BasePageElement(self.driver).input_info(locator2,self.password)

        # self.driver.find_element_by_id('name').send_keys(self.username)
        # self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_css_selector('.span-primary').click()


    def get_login_name(self):
        """
        登录成功后，获取用户名，return str
        """
        # username = self.driver.find_element_by_css_selector('.user_name >.dark').text
        locator = (By.CSS_SELECTOR,'.user_name >.dark')
        text = BasePageElement(self.driver).get_Text(locator)
        return text