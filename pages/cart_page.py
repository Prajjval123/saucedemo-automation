from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# this file handles the cart page
# URL looks like: https://www.saucedemo.com/cart.html
# you get here by clicking the cart icon on the products page

class CartPage(BasePage):

    # --- Locators ---

    # the Checkout button at the bottom of the cart page
    # inspected it → found id="checkout"
    CHECKOUT_BUTTON = (By.ID, "checkout")

    # each item in the cart has this class
    # I use this to count how many items are showing in the cart
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    # --- Actions ---

    def is_on_cart_page(self):
        # URL should contain "cart" when we are on this page
        return "cart" in self.get_current_url()

    def get_cart_items(self):
        # find all cart item elements and return them as a list
        # I use len() on this list to count how many items are in the cart
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEMS))
        return items

    def click_checkout(self):
        # click the Checkout button to start the checkout process
        self.click(self.CHECKOUT_BUTTON)
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)
