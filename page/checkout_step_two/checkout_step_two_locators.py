from selenium.webdriver.common.by import By


class CheckoutStepTwoLocators:
    ITEM_PRICE_TEXT = (By.CSS_SELECTOR, ".inventory_item_price")
    ITEM_TOTAL_TEXT = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX_TEXT = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL_TEXT = (By.CSS_SELECTOR, ".summary_total_label")
    BUTTON_FINISH = (By.CSS_SELECTOR, "button[data-test='finish']")
    COMPLETE_TEXT = (By.CSS_SELECTOR, "h2.complete-header")

    COMPLETE_TEXT_FACT = "Thank you for your order!"
