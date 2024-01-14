import pytest
from selenium import webdriver
from page_objects import FormPage, ResultsPage

@pytest.fixture
def driver():
    return webdriver.Chrome()

def test_fill_and_submit_form(driver):
    form_page = FormPage(driver)
    results_page = ResultsPage(driver)

    form_page.open()
    form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787",
                        "", "Москва", "Россия", "QA", "SkyPro")
    form_page.submit_form()

    assert results_page.is_zip_code_highlighted()
    assert results_page.are_other_fields_highlighted()

    driver.quit()