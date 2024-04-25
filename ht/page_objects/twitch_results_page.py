from selenium.webdriver.common.by import By

from ht.page_objects.base_page import BasePage
from ht.page_objects.twitch_streamer_page import TwitchStreamerPage


class TwitchResultsPage(BasePage):

    streamer_container = (By.CSS_SELECTOR, " #__next section:nth-child(1) >"
                                           " div:nth-child(3) > a:not([href*='channels']) div>h4")
    list_streamers = (By.CSS_SELECTOR, "#__next section:nth-child(1) > div > a:not([href*='channels']) div>h4")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_a_streamer(self):
        self.click(self.streamer_container)
        return TwitchStreamerPage(self.driver)

    def get_streamer_name(self):
        return self.get_text(self.streamer_container)

    def get_results_count(self):
        elements = self.wait_for_elements_visible(self.list_streamers)
        return len(elements)
