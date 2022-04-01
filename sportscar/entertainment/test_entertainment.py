from pytest import mark
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


# class EntertainmentTest:
@mark.entertainment
@mark.ui
def test_can_navigate_to_playwright_docs():
    c = Options()
    # passing headless parameter
    c.add_argument("--headless")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=c)
    browser.get("https://playwright.dev/python/docs/intro")
    browser.close()
    assert True
