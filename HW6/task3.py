from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 4).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container")))

third_image_src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

print(third_image_src)

driver.quit()
