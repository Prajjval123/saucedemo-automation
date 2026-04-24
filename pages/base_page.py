from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# I created this base class because every page needs the same basic actions
# like click, type text, check if something is visible etc.
# Instead of writing the same code in login_page, cart_page, checkout_page separately
# I wrote it once here and all page files just inherit from this

class BasePage:

    def __init__(self, driver):
        # store the driver so every page file can use self.driver
        self.driver = driver

        # WebDriverWait is smarter than time.sleep()
        # it waits ONLY until the element appears (max 15 seconds)
        # instead of always waiting a fixed amount of time
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        # wait until the element is clickable, then click it
        # clickable means: it exists on page AND is not disabled/hidden
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        # wait for the input field to be visible
        # clear whatever is already in it, then type the new text
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        # wait for the element to appear and return the text it shows
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_displayed(self, locator):
        # returns True if element is visible on screen, False if not
        # I wrapped it in try/except because if element doesn't exist at all
        # selenium throws an error - I just want False instead of a crash
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except Exception:
            return False

    def get_current_url(self):
        # returns whatever URL is currently open in the browser
        # I use this to check if the page navigated to the right place
        return self.driver.current_url
