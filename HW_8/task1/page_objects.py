from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class FormPage(BasePage):
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_form(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position, company):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=first-name]").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=last-name]").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=address").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=e-mail]").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=phone]").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=zip-code]").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=city]").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=country]").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=job-position]").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "input[name=company]").send_keys(company)

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "main[class=flex-shrink-2]"))
        )

class ResultsPage(BasePage):
    def is_zip_code_highlighted(self):
        zip_code_field = self.driver.find_element(By.CSS_SELECTOR, "div#zip-code")
        return "alert-danger" in zip_code_field.get_attribute("class")

    def are_other_fields_highlighted(self):
        green_highlighted_fields = self.driver.find_elements(By.CSS_SELECTOR, "div.alert.py-2.alert-success")
        return len(green_highlighted_fields) == 9