import allure

from page.base_page import BasePage
from page.inventory.inventory_locators import InventoryLocators


class InventoryPage(BasePage):
    inventory_locators = InventoryLocators()

    def select_sort(self, sort_value: str):
        with allure.step(f"Отсортировать товар по значению '{sort_value}'"):
            self.select_value_in_menu(
                self.inventory_locators.MENU_PRODUCT_SORT, self.inventory_locators.ITEM_MENU_SORT.get(sort_value),
                "полю сортировки", sort_value
            )

    def add_item_to_cart(self, num: int):
        with allure.step(f"Добавить товар {num} в корзину"):
            self.click_to_element(self.inventory_locators.button_add_to_cart(num), "кнопке 'Add to cart'")

    def go_to_card(self):
        with allure.step("Перейти в корзину"):
            self.click_to_element(self.inventory_locators.CART_IMG, "иконке корзины")

    def count_items_in_page(self):
        return len(self.get_elements(self.inventory_locators.INVENTORY_NAME))
