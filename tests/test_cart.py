import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import VALID_USERNAME, VALID_PASSWORD

# all cart related test cases are here
# before each test I need to be logged in first
# so I created a fixture called "login_first" that handles login automatically

class TestCart:

    @pytest.fixture(autouse=True)
    def login_first(self, driver):
        # autouse=True means this fixture runs automatically before every test in this class
        # I don't have to call it manually in each test
        #
        # it logs in and stores the inventory page so I can use it as self.inventory
        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)
        self.inventory = InventoryPage(driver)

    def test_add_one_item_cart_badge_shows_1(self, driver):
        # what I am testing: after adding 1 item, the cart badge should show "1"

        # add the backpack to cart
        self.inventory.add_to_cart(self.inventory.ADD_BACKPACK_BTN)

        # read the number on the cart badge
        cart_count = self.inventory.get_cart_count()

        assert cart_count == "1", \
            f"cart badge should show 1 after adding one item but showed: {cart_count}"

    def test_add_two_items_cart_badge_shows_2(self, driver):
        # what I am testing: after adding 2 items, the cart badge should show "2"

        self.inventory.add_to_cart(self.inventory.ADD_BACKPACK_BTN)
        self.inventory.add_to_cart(self.inventory.ADD_BIKE_LIGHT_BTN)

        cart_count = self.inventory.get_cart_count()

        assert cart_count == "2", \
            f"cart badge should show 2 after adding two items but showed: {cart_count}"

    def test_clicking_cart_icon_goes_to_cart_page(self, driver):
        # what I am testing: clicking the cart icon should open the cart page
        # I verify this by checking if the URL contains "cart"

        self.inventory.add_to_cart(self.inventory.ADD_BACKPACK_BTN)
        cart_page = self.inventory.go_to_cart()

        assert cart_page.is_on_cart_page(), \
            "clicking cart icon should go to cart page but it did not"

    def test_added_item_appears_in_cart(self, driver):
        # what I am testing: the item I added should actually show up on the cart page
        # end to end check: add item → go to cart → item is there

        self.inventory.add_to_cart(self.inventory.ADD_BACKPACK_BTN)
        cart_page = self.inventory.go_to_cart()

        items_in_cart = cart_page.get_cart_items()

        assert len(items_in_cart) == 1, \
            f"cart page should show 1 item but found {len(items_in_cart)}"
