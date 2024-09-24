import allure

from model.checkout_step_one.checkout_step_one_model import CheckoutStepOneModel
from page.auth.auth_page import AuthPage
from page.cart.cart_page import CartPage
from page.checkout_step_one.checkout_step_one_page import CheckoutStepOnePage
from page.checkout_step_two.checkout_step_two_page import CheckoutStepTwoPage
from page.inventory.inventory_page import InventoryPage
from src.assert_msg import AssertMsg
from src.urls import Urls
from src.user_names import UserNames

"""Оформление заказа."""


@allure.title("E2E: Оформление заказа покупателя")
def test_make_order(driver, logger, first_name, last_name, postcode):
    urls = Urls()
    assert_massage = AssertMsg()
    user_names = UserNames()
    auth_page = AuthPage(driver, logger)
    inventory_page = InventoryPage(driver, logger)
    cart_page = CartPage(driver, logger)
    checkout_step_one_page = CheckoutStepOnePage(driver, logger)
    checkout_step_two_page = CheckoutStepTwoPage(driver, logger)

    auth_page.open_page(urls.URL_BASE)
    auth_page.auth(user_names.STANDARD_USER, user_names.PASSWORD)
    inventory_page.select_sort(inventory_page.inventory_locators.SORT_ZA)
    inventory_page.assert_page_not_empty(inventory_page.count_items_in_page(), assert_massage.NO_ITEMS)
    inventory_page.add_item_to_cart(1)
    inventory_page.add_item_to_cart(2)
    inventory_page.go_to_card()
    cart_page.delete_item_in_cart(2)
    cart_page.click_checkout()
    cart_page.assert_equal_values(urls.URL_CHECKOUT, cart_page.get_current_url(), assert_massage.INVALID_URL)
    checkout_step_one_page.send_order(CheckoutStepOneModel(first_name, last_name, postcode))
    checkout_step_one_page.assert_equal_values(checkout_step_two_page.get_sum_items_price(),
                                               checkout_step_two_page.get_item_total(), assert_massage.WRONG_SUMMA)
    checkout_step_one_page.assert_equal_values(checkout_step_two_page.get_sum_item_total_and_tax(),
                                               checkout_step_two_page.get_total(), assert_massage.WRONG_SUMMA)
    checkout_step_two_page.click_finish()
    checkout_step_two_page.assert_equal_values(checkout_step_two_page.get_complete_text(),
                                               checkout_step_two_page.checkout_step_two_locators.COMPLETE_TEXT_FACT,
                                               assert_massage.WRONG_TEXT_MSG)
