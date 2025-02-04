import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.config_reader import read_config

import yaml

class DriverFactory:
    def __init__(self):
        self.driver = None
        self.browser = read_config().get("browser")
        self.setup_logger()

    def setup_logger(self):
        """Configure a basic logger"""
        self.logger = logging.getLogger("Web UI Automation")
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def create_driver(self):
        """Factory method to create a WebDriver instance"""
        if self.browser["type"] == "chrome":
            options = webdriver.ChromeOptions()
            if self.browser["headless"]:
                options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")

            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=options
            )

        elif self.browser["type"] == "firefox":
            options = webdriver.FirefoxOptions()
            if self.browser["headless"]:
                options.add_argument("--headless")
            options.add_argument("--disable-gpu")

            self.driver = webdriver.Firefox(
                service=Service(GeckoDriverManager().install()), options=options
            )
        
        self.driver.implicitly_wait(self.browser['implicit_wait'])
        self.logger.info(f"Driver created: {self.browser['type']}")

        return self.driver

    def quit_driver(self):
        """Quit the WebDriver"""
        if self.driver:
            self.driver.quit()
            self.logger.info("Driver quit")
