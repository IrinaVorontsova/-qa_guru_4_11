import pytest
from selene.support.shared import browser

from tests.test_page import TestPage


@pytest.fixture(scope='function')
def driver_browser():
    browser.config.window_width = 1600
    browser.config.window_height = 1024
    url = TestPage.set_url()
    browser.open(url)
    yield driver_browser
    browser.close()