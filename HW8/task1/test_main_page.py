from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages import MainPage


def test_color_fields():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.text_name()
    main_page.button("[type='submit']")

    first_name = main_page.first_name()
    last_name = main_page.last_name()
    address = main_page.address()
    zip_code = main_page.zip_code()
    city = main_page.city()
    country = main_page.country()
    e_mail = main_page.e_mail()
    phone = main_page.phone()
    job_position = main_page.job_position()
    company = main_page.company()

    sleep(1)

    assert first_name == "rgba(209, 231, 221, 1)"
    assert last_name == "rgba(209, 231, 221, 1)"
    assert address == "rgba(209, 231, 221, 1)"
    assert zip_code == "rgba(248, 215, 218, 1)"
    assert city == "rgba(209, 231, 221, 1)"
    assert country == "rgba(209, 231, 221, 1)"
    assert e_mail == "rgba(209, 231, 221, 1)"
    assert phone == "rgba(209, 231, 221, 1)"
    assert job_position == "rgba(209, 231, 221, 1)"
    assert company == "rgba(209, 231, 221, 1)"

    browser.quit()