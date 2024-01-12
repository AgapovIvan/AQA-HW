from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Кликаем на кнопку "Add Element" пять раз
    for _ in range(5):
        add_element_button = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
        add_element_button.click()
        time.sleep(1) 

    # Собираем список кнопок "Delete"
    delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')

    # Выводим размер списка на экран
    print(f"Размер списка кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрываем браузер после завершения
    driver.quit()