import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import (
    VALID_USERNAME, VALID_PASSWORD,
    CUSTOMER_FIRST_NAME, CUSTOMER_LAST_NAME, CUSTOMER_ZIP,
    ORDER_SUCCESS_MESSAGE
)

# all checkout related test cases are here
# checkout flow: login → add item → go to cart → click checkout → fill form → finish

class TestCheckout:

    @pytest.fixture(autouse=True)
    def reach_checkout(self, driver):
        # this runs before every test in this class
        # it does all the steps needed to GET to the checkout page
        # so each test can start directly from the checkout form

        # step 1: login
        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)

        # step 2: add one product to cart
        inventory = InventoryPage(driver)
        inventory.add_to_cart(inventory.ADD_BACKPACK_BTN)

        # step 3: go to cart page
        cart_page = inventory.go_to_cart()

        # step 4: click checkout - now we are on checkout step 1
        # store it as self.checkout so all tests below can use it
        self.checkout = cart_page.click_checkout()

    def test_complete_checkout_works(self, driver):
        # what I am testing: filling all details correctly and clicking Finish
        # should complete the order and go to the confirmation page

        self.checkout.fill_customer_info(
            CUSTOMER_FIRST_NAME,
            CUSTOMER_LAST_NAME,
            CUSTOMER_ZIP
        )
        self.checkout.click_continue()
        self.checkout.click_finish()

        assert self.checkout.is_order_complete(), \
            "after clicking Finish, URL should contain 'checkout-complete' but it did not"

    def test_success_message_appears_after_order(self, driver):
        # what I am testing: after placing the order, the page should show
        # "Thank you for your order!" message

        self.checkout.fill_customer_info(
            CUSTOMER_FIRST_NAME,
            CUSTOMER_LAST_NAME,
            CUSTOMER_ZIP
        )
        self.checkout.click_continue()
        self.checkout.click_finish()

        success_text = self.checkout.get_success_message()

        assert ORDER_SUCCESS_MESSAGE in success_text, \
            f"expected '{ORDER_SUCCESS_MESSAGE}' but got: '{success_text}'"

    def test_empty_first_name_shows_error(self, driver):
        # what I am testing: if first name is left blank and I click Continue
        # the app should show a validation error

        self.checkout.fill_customer_info(
            "",                  # I left first name empty on purpose
            CUSTOMER_LAST_NAME,
            CUSTOMER_ZIP
        )
        self.checkout.click_continue()

        error = self.checkout.get_error_message()

        assert "First Name is required" in error, \
            f"expected 'First Name is required' but got: '{error}'"

    def test_empty_last_name_shows_error(self, driver):
        # what I am testing: leaving last name blank should show validation error

        self.checkout.fill_customer_info(
            CUSTOMER_FIRST_NAME,
            "",                  # last name left empty
            CUSTOMER_ZIP
        )
        self.checkout.click_continue()

        error = self.checkout.get_error_message()

        assert "Last Name is required" in error, \
            f"expected 'Last Name is required' but got: '{error}'"

    def test_empty_zip_shows_error(self, driver):
        # what I am testing: leaving zip code blank should show validation error

        self.checkout.fill_customer_info(
            CUSTOMER_FIRST_NAME,
            CUSTOMER_LAST_NAME,
            ""                   # zip code left empty
        )
        self.checkout.click_continue()

        error = self.checkout.get_error_message()

        assert "Postal Code is required" in error, \
            f"expected 'Postal Code is required' but got: '{error}'"
