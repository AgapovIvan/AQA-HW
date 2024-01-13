from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

input_field.clear()

input_field.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button_text)

driver.quit()
