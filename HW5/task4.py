from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def close_modal():
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get("http://the-internet.herokuapp.com/entry_ad")

        # Подождем, чтобы модальное окно полностью загрузилось
        time.sleep(2)

        # Находим кнопку "Close" и кликаем на нее
        close_button = driver.find_element(By.CSS_SELECTOR, 'div.modal-footer')
        close_button.click()

        # Подождем, чтобы модальное окно закрылось
        time.sleep(2)

    finally:
        # Закрываем браузер после завершения
        driver.quit()

# Запускаем скрипт
close_modal()
