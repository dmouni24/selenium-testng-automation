
from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")

    def search(self, text):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(text)
        self.driver.find_element(*self.SEARCH_INPUT).submit()
