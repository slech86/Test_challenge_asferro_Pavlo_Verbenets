import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def chrome_options():
    options = Options()
    options.add_argument('chrome')  # 'headless', 'chrome'
    options.add_argument('--window-size=1600,900')
    return options


@pytest.fixture(scope="function")
def browser(chrome_options):
    options = chrome_options
    s = Service('drivers/chromedriver')
    browser = webdriver.Chrome(service=s, options=options)
    yield browser
    browser.quit()
