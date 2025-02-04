import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage
from utils.config_reader import read_config

from utils.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def driver():
    """Fixture to set up and tear down the driver"""
    driver_factory = DriverFactory()
    driver = driver_factory.create_driver()
    yield driver
    driver_factory.quit_driver()

def test_login(driver):
    driver.get(read_config().get("selenium").get("base_url"))
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Check for some condition that verifies login was successful
    assert "Swag Labs" in driver.title
