import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture
def driver():
    return webdriver.Chrome()

def test_slow_calculator(driver):
    calculator_page = CalculatorPage(driver)

    calculator_page.open()
    calculator_page.enter_delay_value("45")
    calculator_page.perform_calculation(7, "+", 8)
    calculator_page.get_result_after_delay(15, 45)

    driver.quit()