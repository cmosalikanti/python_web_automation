from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver(browser_name: str = 'chrome'):
    if browser_name.lower() == 'chrome':
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Running headless, you can remove this if you want the UI
        return webdriver.Chrome(service=service, options=options)

    elif browser_name.lower() == 'firefox':
        service = Service(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        return webdriver.Firefox(service=service, options=options)
    
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

