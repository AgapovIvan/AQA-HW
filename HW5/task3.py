from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def click_blue_button():
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get("http://uitestingplayground.com/classattr")

        # Кликаем на синюю кнопку
        blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
        blue_button.click()

        # Даем время для анимации и обновления страницы
        time.sleep(1)

    finally:
        # Закрываем браузер после завершения
        driver.quit()

# Запускаем скрипт три раза подряд
for _ in range(3):
    click_blue_button()