from ht.page_objects.twitch_main_page import TwitchMainPage
from ht.tests.base_test import BaseTest


class TestTwitch(BaseTest):

    def test_twitch(self):
        search_item = "StarCraft 2"

        twitch_main_page = TwitchMainPage(self.driver)
        assert twitch_main_page.get_title() == "Twitch"
        assert twitch_main_page.get_current_url() == "https://m.twitch.tv/"
        twitch_main_page.accept_privacy().trigger_search()

        twitch_results_page = twitch_main_page.search_for(search_item)
        twitch_results_page.wait_for_page_to_be_loaded()
        assert twitch_results_page.get_results_count() > 0
        twitch_results_page.scroll_down(2)

        name_from_results_page = twitch_results_page.get_streamer_name()
        streamer_page = twitch_results_page.click_a_streamer()
        streamer_page.wait_for_page_to_be_loaded()
        name_from_personal_page = streamer_page.get_name_own_page()

        assert name_from_results_page == name_from_personal_page
        assert streamer_page.has_video() is True
        assert streamer_page.has_avatar_icon() is True
        assert streamer_page.has_share_button() is True
        assert streamer_page.has_follow_button() is True

        streamer_page.take_screenshot()
