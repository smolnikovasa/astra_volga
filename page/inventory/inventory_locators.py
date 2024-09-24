from selenium.webdriver.common.by import By


class InventoryLocators:
    """Селекторы страницы https://www.saucedemo.com/inventory.html."""

    SORT_ZA = "Name (Z to A)"

    MENU_PRODUCT_SORT = (By.CSS_SELECTOR, "select.product_sort_container")
    ITEM_MENU_SORT = {SORT_ZA: (By.CSS_SELECTOR, "option[value='za']")}
    CART_IMG = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    INVENTORY_NAME = (By.CSS_SELECTOR, "div.inventory_item_name ")

    @staticmethod
    def button_add_to_cart(num: int) -> tuple:
        return By.XPATH, f"(//button[@class='btn btn_primary btn_small btn_inventory '])[{num}]"
