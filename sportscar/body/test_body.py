from pytest import mark
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


@mark.body
class BodyTest:

    @mark.smoke
    @mark.ui
    def test_can_navigate_to_playwright_docs(self):
        c = Options()
        # passing headless parameter
        c.add_argument("--headless")
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=c)
        browser.get("https://playwright.dev/python/docs/intro")
        browser.close()
        assert True
