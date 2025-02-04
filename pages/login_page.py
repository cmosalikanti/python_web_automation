from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        self.send_keys(*self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(*self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click_element(*self.LOGIN_BUTTON)
