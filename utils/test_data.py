# I keep all test data in one file so I don't have to change it in 10 places
# if something changes, I just update it here

# saucedemo gives these credentials on their website for testing purposes
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

# these don't exist - used to test what happens when wrong credentials are entered
INVALID_USERNAME = "wrong_user"
INVALID_PASSWORD = "wrong_password"

# saucedemo has a special locked user to test the locked out scenario
LOCKED_USERNAME = "locked_out_user"

# dummy customer info for filling the checkout form
CUSTOMER_FIRST_NAME = "John"
CUSTOMER_LAST_NAME  = "Doe"
CUSTOMER_ZIP        = "10001"

# these are the exact error messages saucedemo shows
# I copied these by actually running the site and reading the error text
ERROR_WRONG_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
ERROR_LOCKED_USER       = "Epic sadface: Sorry, this user has been locked out."
ERROR_EMPTY_USERNAME    = "Epic sadface: Username is required"
ERROR_EMPTY_PASSWORD    = "Epic sadface: Password is required"

# success message shown after order is placed
ORDER_SUCCESS_MESSAGE = "Thank you for your order!"
