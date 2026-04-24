from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# this file handles everything related to the login page of saucedemo
# it has two things: locators (how to find elements) and actions (what to do)

class LoginPage(BasePage):

    # the URL I want to open
    URL = "https://www.saucedemo.com"

    # --- Locators ---
    # I found these by opening saucedemo.com in Chrome
    # then right clicking on each element and clicking Inspect
    # in the HTML I could see the id or class name for each element

    # right clicked username box → inspected → found id="user-name"
    USERNAME_INPUT = (By.ID, "user-name")

    # right clicked password box → inspected → found id="password"
    PASSWORD_INPUT = (By.ID, "password")

    # right clicked login button → inspected → found id="login-button"
    LOGIN_BUTTON = (By.ID, "login-button")

    # when login fails, a red error box appears
    # inspected it → found class="error-message-container"
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    # --- Actions ---

    def open(self):
        # open the login page URL in the browser
        self.driver.get(self.URL)
        return self  # returning self lets me write page.open().login() in one line

    def login(self, username, password):
        # type username, type password, click login button
        # this is what a real user does manually - we are just automating it
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def is_error_displayed(self):
        # check if the red error box is visible after a failed login
        return self.is_displayed(self.ERROR_MESSAGE)

    def get_error_message(self):
        # read and return the actual error text shown on screen
        return self.get_text(self.ERROR_MESSAGE)
