import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    timeout = 10

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def open_page(self, url):
        with allure.step(f"Открыть в браузере страницу {url}"):
            self.driver.get(url)

    def get_elements(self, locator) -> list:
        with allure.step(f"Найти элементы {locator}"):
            return self.driver.find_elements(*locator)

    def get_element(self, locator) -> WebElement:
        with allure.step(f"Найти элемент {locator}"):
            return self.driver.find_element(*locator)

    def get_text_element(self, locator) -> str:
        with allure.step(f"Получить текст элемента {locator}"):
            return self.get_element(locator).text

    def get_text_elements(self, locator) -> list:
        with allure.step(f"Получить текст элементов {locator}"):
            return list([el.text for el in self.get_elements(locator)])

    def fill_field(self, locator, name, value):
        with allure.step(f"Заполнить поле '{name}' значением {value}"):
            self._element_is_visibility(locator).send_keys(value)

    def click_to_element(self, locator, name):
        with allure.step(f"Кликнуть по '{name}'"):
            self._element_is_clickable(locator).click()

    def select_value_in_menu(self, locator1, locator2, name1, name2):
        with allure.step(f"В меню '{name1}' выбрать значение '{name2}'"):
            self.click_to_element(locator1, name1)
            self.click_to_element(locator2, name2)

    def get_current_url(self):
        with allure.step(f"Получить адрес открытой страницы в браузере"):
            return self.driver.current_url

    def _element_is_visibility(self, locator, timeout=timeout) -> WebElement:
        self.logger.info(f"Дождаться появления элемента {locator}")
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def _element_is_clickable(self, locator, timeout=timeout) -> WebElement:
        self.logger.info(f"Дождаться кликабельности кнопки {locator}")
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    @staticmethod
    def assert_equal_values(value1, value2, assert_msg):
        with allure.step(f"Проверить на равенство значений '{value1}' и '{value2}'"):
            assert value1 == value2, assert_msg

    @staticmethod
    def assert_page_not_empty(value, assert_msg):
        with allure.step(f"Проверить наличие позиций на странице"):
            assert value > 0, assert_msg
