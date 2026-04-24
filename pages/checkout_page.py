from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

# this file handles the checkout flow
# checkout has 3 steps on saucedemo:
#
# Step 1: fill your details (first name, last name, zip code)
# Step 2: review the order summary -> click Finish
# Step 3: confirmation page shows "Thank you for your order!"

class CheckoutPage(BasePage):

    # --- Locators for Step 1 (the form where you fill your info) ---

    # found by inspecting each input field on the checkout form
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT  = (By.ID, "last-name")
    ZIP_CODE_INPUT   = (By.ID, "postal-code")

    # the Continue button that takes you from step 1 to step 2
    CONTINUE_BUTTON  = (By.ID, "continue")

    # error message shown when a required field is left empty
    # found by inspecting the red error element after submitting empty form
    ERROR_MESSAGE    = (By.XPATH, "//h3[@data-test='error']")

    # --- Locators for Step 2 (order summary page) ---

    # the Finish button that places the order
    FINISH_BUTTON    = (By.ID, "finish")

    # --- Locators for Step 3 (confirmation page) ---

    # the big heading that says "Thank you for your order!"
    SUCCESS_HEADER   = (By.CLASS_NAME, "complete-header")

    # --- Actions ---

    def fill_customer_info(self, first_name, last_name, zip_code):
        # fill in all three fields in the customer info form
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.ZIP_CODE_INPUT, zip_code)
        return self

    def click_continue(self):
        # before clicking Continue, dismiss the password popup if it appeared
        # saucedemo uses a known breached password which Chrome warns about
        # we dismiss it here so it doesn't block the Continue button
        self.driver.dismiss_popup()

        # small wait to let the page settle before clicking
        time.sleep(1)

        self.click(self.CONTINUE_BUTTON)
        return self

    def click_finish(self):
        # dismiss popup again just in case it reappeared on the summary page
        self.driver.dismiss_popup()

        # small wait for the order summary page to fully load
        # without this selenium sometimes tries to click before page is ready
        time.sleep(2)

        self.click(self.FINISH_BUTTON)
        return self

    def is_order_complete(self):
        # after order is placed, URL contains "checkout-complete"
        return "checkout-complete" in self.get_current_url()

    def get_success_message(self):
        # read the success message shown on the confirmation page
        return self.get_text(self.SUCCESS_HEADER)

    def get_error_message(self):
        # read the validation error when a required field is left empty
        return self.get_text(self.ERROR_MESSAGE)