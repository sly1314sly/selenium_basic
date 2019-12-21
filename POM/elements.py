from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    
    def __init__(self, driver):
        self.driver = driver



    def get_Text(locator):
        ele = WebDriverWait(driver, 100).until(self.driver.find_element(locator))
        return ele.text

    # def __get__(self, obj, owner):
    #     """Gets the text of the specified object"""
    #     driver = obj.driver
    #     WebDriverWait(driver, 100).until(
    #         lambda driver: driver.find_element_by_css_selector(self.locator))
    #     element = driver.find_element_by_css_selector(self.locator)
    #     return element.get_attribute("value")