from selenium.webdriver.common.by import By


class CheckoutStepOneLocators:
    """Селекторы страницы https://www.saucedemo.com/checkout-step-one.html."""

    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    FIELD_POSTAL_CODE = (By.CSS_SELECTOR, "input[placeholder='Zip/Postal Code']")
    BUTTON_CONTINUE = (By.NAME, "continue")
