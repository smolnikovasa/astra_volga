import allure

from page.auth.auth_locators import AuthLocators
from page.base_page import BasePage


class AuthPage(BasePage):
    """Класс для представления страницы авторизации https://www.saucedemo.com/."""

    auth_locators = AuthLocators()

    def auth(self, login: str, password: str):
        with allure.step(f"Авторизоваться на странице под пользователем {login}"):
            self.fill_field(self.auth_locators.FIELD_USER, 'Username', login)
            self.fill_field(self.auth_locators.FIELD_PASSWORD, 'Password', password)
            self.click_to_element(self.auth_locators.BUTTON_LOGIN, 'кнопке Login')
