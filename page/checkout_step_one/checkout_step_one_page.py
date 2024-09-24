import allure

from model.checkout_step_one.checkout_step_one_model import CheckoutStepOneModel
from page.base_page import BasePage
from page.checkout_step_one.checkout_step_one_locators import CheckoutStepOneLocators


class CheckoutStepOnePage(BasePage):
    checkout_locators = CheckoutStepOneLocators()

    def send_order(self, person_data: CheckoutStepOneModel):
        with allure.step(f"Заполнить форму заказа"):
            self.fill_field(self.checkout_locators.FIELD_FIRST_NAME, 'First Name', person_data.first_name)
            self.fill_field(self.checkout_locators.FIELD_LAST_NAME, 'Last Name', person_data.last_name)
            self.fill_field(self.checkout_locators.FIELD_POSTAL_CODE, 'Zip/Postal Code', person_data.postal_code)
            self.click_to_element(self.checkout_locators.BUTTON_CONTINUE, 'кнопке Continue')
