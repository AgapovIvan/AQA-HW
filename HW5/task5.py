from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def manipulate_input_field():
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get("http://the-internet.herokuapp.com/inputs")

        # Находим поле ввода по тегу и вводим текст "1000"
        input_field = driver.find_element(By.CSS_SELECTOR, 'input')
        input_field.send_keys("1000")

        # Даем время для просмотра введенного текста
        time.sleep(2)

        # Очищаем поле ввода
        input_field.clear()

        # Вводим текст "999" в очищенное поле
        input_field.send_keys("999")

        # Даем время для просмотра введенного текста
        time.sleep(2)

    finally:
        # Закрываем браузер после завершения
        driver.quit()

# Запускаем скрипт
manipulate_input_field()
