from selenium.webdriver.common.by import By

from ht.page_objects.base_page import BasePage


class TwitchStreamerPage(BasePage):

    streamer_avatar = (By.CSS_SELECTOR, "div[class*='tw-avatar']")
    streamer_name = (By.CSS_SELECTOR, "p[title]")
    streamer_heart = (By.CSS_SELECTOR, "div[data-a-selector*='icon']>svg")
    streamer_share = (By.CSS_SELECTOR, "button[aria-label='Share']")
    streamer_video = (By.CSS_SELECTOR, "div>video")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def has_avatar_icon(self):
        return self.isDisplayed(self.streamer_avatar)

    def get_name_own_page(self):
        return self.get_text(self.streamer_name)

    def has_follow_button(self):
        return self.isDisplayed(self.streamer_heart)

    def has_share_button(self):
        return self.isDisplayed(self.streamer_share)

    def has_video(self):
        return self.isDisplayed(self.streamer_video)

