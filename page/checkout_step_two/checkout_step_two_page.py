import allure

from page.base_page import BasePage
from page.checkout_step_two.checkout_step_two_locators import CheckoutStepTwoLocators


class CheckoutStepTwoPage(BasePage):
    """Класс для представления страницы https://www.saucedemo.com/checkout-step-two.html."""

    checkout_step_two_locators = CheckoutStepTwoLocators()

    def get_item_total(self) -> float:
        with allure.step(f"Получить значение 'Item total'"):
            return float(self.parse_string(self.get_text_element(self.checkout_step_two_locators.ITEM_TOTAL_TEXT)))

    def get_tax(self) -> float:
        with allure.step(f"Получить значение 'Tax'"):
            return float(self.parse_string(self.get_text_element(self.checkout_step_two_locators.TAX_TEXT)))

    def get_total(self) -> float:
        with allure.step(f"Получить значение 'Total'"):
            return float(self.parse_string(self.get_text_element(self.checkout_step_two_locators.TOTAL_TEXT)))

    def get_sum_item_total_and_tax(self) -> float:
        with allure.step(f"Получить значение суммы 'Item total' и 'Tax'"):
            return self.get_item_total() + self.get_tax()

    def get_sum_items_price(self) -> float:
        with allure.step(f"Получить общую сумму по товарам"):
            return sum(list([float(self.parse_string(el)) for el in
                             self.get_text_elements(self.checkout_step_two_locators.ITEM_PRICE_TEXT)]))

    def click_finish(self):
        with allure.step(f"Завершить заказ"):
            self.click_to_element(self.checkout_step_two_locators.BUTTON_FINISH, 'кнопке Finish')

    def get_complete_text(self):
        with allure.step(f"Получить текст завершения заказа"):
            return self.get_text_element(self.checkout_step_two_locators.COMPLETE_TEXT)

    @staticmethod
    def parse_string(price_text) -> float:
        return float(price_text.split('$')[1])
