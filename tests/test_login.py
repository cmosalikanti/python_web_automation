import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from drivers.driver_setup import get_driver
from pages.login_page import LoginPage
from utils.config_reader import read_config

@pytest.fixture(scope="module")
def driver():
    config = read_config()
    driver = get_driver(config["browser"])
    driver.get(config["url"])
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Check for some condition that verifies login was successful
    assert "Swag Labs" in driver.title
