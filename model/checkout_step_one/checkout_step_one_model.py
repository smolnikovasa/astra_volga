from dataclasses import dataclass


@dataclass
class CheckoutStepOneModel:
    """Модель данных страницы https://www.saucedemo.com/checkout-step-one.html."""
    first_name: str = ''
    last_name: str = ''
    postal_code: str = ''
