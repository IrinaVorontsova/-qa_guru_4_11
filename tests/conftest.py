import os
import pytest
from selene.support.shared import config
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

    @pytest.fixture(scope='session', autouse=True)
    def load_env():
        load_dotenv()

    @pytest.fixture
    def setup_browser(set_selenoid):
        config.window_width = 1920
        config.window_height = 1080
        config.base_url = 'https://demoqa.com/automation-practice-form'
        browser.config.driver = set_selenoid
        yield
        attach.add_screenshot(browser)
        attach.add_html(browser)
        attach.add_logs(browser)
        attach.add_video(browser)

        browser.quit()

    @pytest.fixture
    def set_selenoid():
        options = Options()
        browser_version = config.getoption('--browser_version')
        browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

        chrome_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(chrome_capabilities)

        return webdriver.Remote(
            command_executor=f"https://{os.getenv('LOGIN')}:{os.getenv('PASSWORD')}@selenoid.autotests.cloud/wd/hub",
            options=options)
