from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_to_page():
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get("http://the-internet.herokuapp.com/login")

        # Находим поле username и вводим значение "tomsmith"
        username_field = driver.find_element(By.CSS_SELECTOR, 'input#username')
        username_field.send_keys("tomsmith")

        # Находим поле password и вводим значение "SuperSecretPassword!"
        password_field = driver.find_element(By.CSS_SELECTOR, 'input#password')
        password_field.send_keys("SuperSecretPassword!")

        # Нажимаем кнопку Login
        login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
        login_button.click()

        # Даем время для просмотра результата
        time.sleep(3)

    finally:
        # Закрываем браузер после завершения
        driver.quit()

# Запускаем скрипт
login_to_page()
