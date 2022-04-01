from pytest import fixture

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


@fixture(scope='session')
def chrome_browser():
    c = Options()
    # passing headless parameter
    c.add_argument("--headless")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                               options=c)
    yield browser


@fixture(scope='function')
def firefox_browser():
    c = Options()
    # passing headless parameter
    c.add_argument("--headless")
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=c)
    yield browser
