from selenium.webdriver.common.by import By


class AuthLocators:
    """Селекторы страницы авторизации https://www.saucedemo.com/."""

    FIELD_USER = (By.XPATH, "//*[@id='user-name']")
    FIELD_PASSWORD = (By.XPATH, "//*[@id='password']")
    BUTTON_LOGIN = (By.XPATH, "//*[@id='login-button']")
