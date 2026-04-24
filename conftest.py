import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# this file runs automatically before and after every test
# pytest picks it up on its own - I don't need to import it anywhere

@pytest.fixture
def driver():

    # Chrome options let us customize the browser before it opens
    chrome_options = Options()

    # create a brand new empty Chrome profile every time tests run
    # this prevents Chrome from loading any saved passwords or settings
    # that could trigger popups during tests
    chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    # tell Chrome not to show the "save password" bubble after login
    chrome_options.add_argument("--disable-save-password-bubble")

    # disable notifications so no permission popups appear
    chrome_options.add_argument("--disable-notifications")

    # skip the "welcome to Chrome" screen on first launch
    chrome_options.add_argument("--no-first-run")

    # disable the password leak detection feature
    # this is what triggers the "Change your password" popup
    # saucedemo uses a known test password (secret_sauce) which Chrome
    # flags as "found in a data breach" - we disable this check entirely
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")

    # more settings to fully turn off password manager and safe browsing alerts
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False
    })

    # open Chrome with all the options we set above
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # open in full screen so all buttons and elements are visible
    driver.maximize_window()

    # wait up to 10 seconds for elements to load before giving up
    driver.implicitly_wait(10)

    # safety net - if the "Change your password" popup somehow still appears
    # this will automatically find the OK button and click it to dismiss it
    # so it doesn't block the test from running
    # we wrap in try/except because if the popup doesn't appear we don't want to crash
    def dismiss_password_popup():
        try:
            ok_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//cr-button[contains(., 'OK')] | //button[contains(., 'OK')]")
                )
            )
            ok_btn.click()
        except Exception:
            pass  # popup did not appear - that's fine, move on

    # attach this function to the driver so any test can call driver.dismiss_popup()
    # if needed
    driver.dismiss_popup = dismiss_password_popup

    # yield means: run the test now
    # everything above yield = setup (before test)
    # everything below yield = cleanup (after test)
    yield driver

    # close Chrome after the test finishes
    driver.quit()