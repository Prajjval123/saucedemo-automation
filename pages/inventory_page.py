from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# this file handles the products/inventory page
# this is the page you see after logging in successfully
# URL looks like: https://www.saucedemo.com/inventory.html

class InventoryPage(BasePage):

    # --- Locators ---

    # the cart icon at top right corner of the page
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    # the small number badge on the cart icon that shows how many items are added
    # this only appears after at least one item is added
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # each product has its own "Add to cart" button with a unique id
    # I found these by going to the products page and inspecting each button
    # the id format is: add-to-cart-[product-name]
    ADD_BACKPACK_BTN   = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT_BTN = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_TSHIRT_BTN     = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")

    # --- Actions ---

    def is_on_inventory_page(self):
        # after login, URL should contain "inventory"
        # if it does, login was successful
        return "inventory" in self.get_current_url()

    def add_to_cart(self, button_locator):
        # click whichever add to cart button is passed in
        # example usage: inventory.add_to_cart(inventory.ADD_BACKPACK_BTN)
        self.click(button_locator)

    def get_cart_count(self):
        # read the number shown on the cart badge
        # returns a string like "1" or "2"
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        # click the cart icon to go to the cart page
        self.click(self.CART_ICON)
        # import here to avoid circular imports between page files
        from pages.cart_page import CartPage
        return CartPage(self.driver)
