from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):
    
    def __init__(self, driver):
        self.driver = driver



    def get_Text(self,locator):
        ele = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(locator))
        return ele.text

    def input_info(self,locator,concent):
        ele = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(locator))
        ele.clear()
        ele.send_keys(concent)

    # def __get__(self, obj, owner):
    #     """Gets the text of the specified object"""
    #     driver = obj.driver
    #     WebDriverWait(driver, 100).until(
    #         lambda driver: driver.find_element_by_css_selector(self.locator))
    #     element = driver.find_element_by_css_selector(self.locator)
    #     return element.get_attribute("value")
    