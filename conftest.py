from pytest import fixture

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


@fixture(scope='function')
def chrome_browser():
    c = Options()
    # passing headless parameter
    c.add_argument("--headless")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                               options=c)
    return browser


@fixture(scope='session')
def firefox_browser():
    c = Options()
    # passing headless parameter
    c.add_argument("--headless")
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=c)
    yield browser


@fixture(scope='function')
def edge_browser():
    c = Options()
    # passing headless parameter
    c.add_argument("--headless")
    browser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=c)
    yield browser


@fixture(scope='function')
def brave_browser():
    c = Options()
    # passing headless parameter
    c.add_argument("--headless")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=c)
    yield browser


@fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True
    }
