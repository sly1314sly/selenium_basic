from po.element import BasePageElement
from po.locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'

class InputUsername(BasePageElement):
    locator= 'name'

class InputPassword(BasePageElement):
    locator = 'pass'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()
    input_username = InputUsername()
    input_password = InputPassword()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def is_cnode_matches(self):
        return 'Cnode ' in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

    def is_user_login_suceess(self,username):
        return username in self.driver.page_source