from selenium.webdriver.common.by import By

from ht.page_objects.base_page import BasePage
from ht.page_objects.twitch_results_page import TwitchResultsPage


class TwitchMainPage(BasePage):

    privacy_button = (By.CSS_SELECTOR, "div[class*='tw-modal'] button")
    search_button = (By.CSS_SELECTOR, "nav a[href*='search']")
    search_inputField = (By.CSS_SELECTOR, "input[data-a-target='tw-input']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def accept_privacy(self):
        self.click(self.privacy_button)
        return self

    def trigger_search(self):
        self.click(self.search_button)
        return self

    def search_for(self, value):
        self.type_and_go(self.search_inputField, value)
        return TwitchResultsPage(self.driver)

