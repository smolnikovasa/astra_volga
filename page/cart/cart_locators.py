from selenium.webdriver.common.by import By


class CartLocators:
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "button.checkout_button ")

    @staticmethod
    def button_remove(num: int) -> tuple:
        return By.XPATH, f"(//button[@class='btn btn_secondary btn_small cart_button'])[{num}]"
