import time
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

timeout = 10
polling_frequency = 0.5


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element_visible(self, by_locator):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(by_locator))

    def wait_for_elements_visible(self, by_locator):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(by_locator))

    def wait_for_page_to_load(self, by_locator):
        try:
            WebDriverWait(self.driver, timeout, polling_frequency).until(ec.presence_of_element_located(by_locator))
        except TimeoutException:
            print("Page was not loaded successfully.")

    def wait_for_page_to_be_loaded(self):
        time.sleep(1)
        ct = 0
        state = self.driver.execute_script("return document.readyState;")
        while ct < timeout and state != "complete":
            ct += 1
            time.sleep(0.5)
            state = self.driver.execute_script("return document.readyState;")

    def isDisplayed(self, by_locator):
        return self.wait_for_element_visible(by_locator).is_displayed()

    def click(self, by_locator):
        self.wait_for_element_visible(by_locator).click()

    def type_and_go(self, by_locator, value):
        print("\nTyping: " + value)
        el = self.wait_for_element_visible(by_locator)
        el.clear()
        el.send_keys(value)
        el.send_keys(Keys.RETURN)

    def get_text(self, by_locator):
        element = self.wait_for_element_visible(by_locator)
        text = element.text
        print("\nElement text is: " + text)
        return text

    def scroll_down(self, times):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(1)

    def scroll_down_alt(self, by_locator, times):
        container = self.wait_for_elements_visible(by_locator)
        for _ in range(times):
            container[0].send_keys(Keys.END)
            time.sleep(1)

    def take_screenshot(self):
        print("\nTaking a screenshot.")
        self.driver.save_screenshot("scn.png")

