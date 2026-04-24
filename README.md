# SauceDemo Automation Project

Selenium + Python test automation for [SauceDemo](https://www.saucedemo.com)
SauceDemo is a demo e-commerce site built specifically for practising test automation.

---

## What I automated

| Module   | Test Cases | What is covered |
|----------|-----------|-----------------|
| Login    | 6 | valid login, wrong credentials, locked user, empty username, empty password |
| Cart     | 4 | add one item, add two items, navigate to cart, item shows in cart |
| Checkout | 5 | full order flow, success message, empty first name, empty last name, empty zip |

**Total: 15 test cases**

---

## Folder structure

```
saucedemo-automation/
│
├── pages/
│   ├── base_page.py       → common methods used by all pages (click, type, wait)
│   ├── login_page.py      → login page locators and actions
│   ├── inventory_page.py  → products page locators and actions
│   ├── cart_page.py       → cart page locators and actions
│   └── checkout_page.py   → checkout flow locators and actions
│
├── tests/
│   ├── test_login.py      → 6 login test cases
│   ├── test_cart.py       → 4 cart test cases
│   └── test_checkout.py   → 5 checkout test cases
│
├── utils/
│   └── test_data.py       → all usernames, passwords, expected messages in one place
│
├── conftest.py            → opens Chrome before each test, closes after
├── pytest.ini             → tells pytest where to find tests
└── requirements.txt       → libraries needed to run the project
```

---

## How to run

```bash
# install libraries (only needed once)
pip install -r requirements.txt

# run all tests
pytest

# run only login tests
pytest tests/test_login.py

# run only cart tests
pytest tests/test_cart.py

# run only checkout tests
pytest tests/test_checkout.py
```

---

## Tech used
- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model pattern
- WebDriver Manager
