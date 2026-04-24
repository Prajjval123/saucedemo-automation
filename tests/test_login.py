from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import (
    VALID_USERNAME, VALID_PASSWORD,
    INVALID_USERNAME, INVALID_PASSWORD,
    LOCKED_USERNAME,
    ERROR_WRONG_CREDENTIALS,
    ERROR_LOCKED_USER,
    ERROR_EMPTY_USERNAME,
    ERROR_EMPTY_PASSWORD
)

# all login related test cases are grouped here in one class
# each function starting with test_ is one test case
# pytest automatically finds and runs all of them

class TestLogin:

    def test_valid_login(self, driver):
        # what I am testing: valid username and password should redirect to inventory page
        #
        # steps:
        # 1. open the login page
        # 2. type valid username and password
        # 3. click Login
        # 4. check that URL now contains "inventory" - means login worked

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)

        # assert checks if something is true
        # if it is true → test passes
        # if it is false → test fails and shows the message I wrote
        assert inventory_page.is_on_inventory_page(), \
            "login with valid credentials should go to inventory page but it did not"

    def test_wrong_credentials_shows_error(self, driver):
        # what I am testing: wrong username/password should show a red error message

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

        assert login_page.is_error_displayed(), \
            "a red error message should appear when wrong credentials are used"

    def test_wrong_credentials_error_text_is_correct(self, driver):
        # what I am testing: not just that an error appeared, but that it says the RIGHT thing
        # I want to verify the exact error message text matches what saucedemo shows

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

        actual_error = login_page.get_error_message()

        assert ERROR_WRONG_CREDENTIALS in actual_error, \
            f"expected error: '{ERROR_WRONG_CREDENTIALS}' but got: '{actual_error}'"

    def test_locked_user_cannot_login(self, driver):
        # what I am testing: saucedemo has a user called locked_out_user
        # this user is blocked from logging in
        # the app should show a specific locked out error message

        login_page = LoginPage(driver)
        login_page.open()

        # using valid password but the locked username
        login_page.login(LOCKED_USERNAME, VALID_PASSWORD)

        actual_error = login_page.get_error_message()

        assert ERROR_LOCKED_USER in actual_error, \
            f"expected locked out message but got: '{actual_error}'"

    def test_empty_username_shows_error(self, driver):
        # what I am testing: leaving username blank and clicking login should show error
        # I pass "" (empty string) as the username to simulate leaving it blank

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", VALID_PASSWORD)  # empty username

        actual_error = login_page.get_error_message()

        assert ERROR_EMPTY_USERNAME in actual_error, \
            f"expected 'Username is required' error but got: '{actual_error}'"

    def test_empty_password_shows_error(self, driver):
        # what I am testing: leaving password blank should show validation error

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USERNAME, "")  # empty password

        actual_error = login_page.get_error_message()

        assert ERROR_EMPTY_PASSWORD in actual_error, \
            f"expected 'Password is required' error but got: '{actual_error}'"
