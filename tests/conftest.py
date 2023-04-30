import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
import os

from utils import attach


DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='class', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='class')
def setup_browser(set_driver):
    # browser.config.driver = set_driver
    setup_browser = Browser(Config(set_driver))
    yield setup_browser

    attach.add_html(setup_browser)
    attach.add_screenshot(setup_browser)
    attach.add_logs(setup_browser)
    attach.add_video(setup_browser)
    setup_browser.quit()

@pytest.fixture(scope='class')
def set_driver(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    return webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )