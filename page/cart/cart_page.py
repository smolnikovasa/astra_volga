import allure

from page.base_page import BasePage
from page.cart.cart_locators import CartLocators


class CartPage(BasePage):
    cart_locators = CartLocators()

    def delete_item_in_cart(self, num):
        with allure.step(f"Удалить товар {num} из корзины"):
            self.click_to_element(self.cart_locators.button_remove(num), "кнопке 'Remove'")

    def click_checkout(self):
        with allure.step(f"Перейти к оформлению заказа"):
            self.click_to_element(self.cart_locators.BUTTON_CHECKOUT, "кнопке 'Checkout'")
