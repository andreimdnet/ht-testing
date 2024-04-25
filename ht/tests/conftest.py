import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ht.utils.test_data import TestData


@pytest.fixture(scope="class")
def setup(request):
    print("\nEmulating: " + TestData.mobile_nexus_5)
    emulate_mobile = {"deviceName": TestData.mobile_nexus_5}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", emulate_mobile)
    chrome_service = ChromeService(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    _driver.get(TestData.url)
    request.cls.driver = _driver
    yield request.cls.driver
    request.cls.driver.quit()
