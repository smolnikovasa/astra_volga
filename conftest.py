import allure
import os
import pytest

from selenium import webdriver
from logger import Logger
from faker import Faker

_logger = None


@pytest.fixture()
def logger():
    """Получить базовый логгер."""
    global _logger
    if _logger is None:
        _logger = Logger.get_logger()
    return _logger


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Передача опции указания пути к каталогу для сохранения allure файлов с результатами тестов."""
    cwd_report = os.path.join(os.path.dirname(os.path.abspath(__file__)), "allure-result")
    allure_dir = getattr(config.option, "allure_report_dir", None)
    if not allure_dir:
        setattr(config.option, "allure_report_dir", cwd_report)


@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    failed_before = request.session.testsfailed

    yield driver

    if request.session.testsfailed != failed_before:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture
def first_name():
    """Генератор имени."""
    return Faker().first_name()


@pytest.fixture
def last_name():
    """Генератор фамилии."""
    return Faker().last_name()


@pytest.fixture
def postcode():
    """Генератор почтового индекса."""
    return Faker().postcode()
