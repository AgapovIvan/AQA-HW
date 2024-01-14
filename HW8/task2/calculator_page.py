from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import BasePage

class CalculatorPage(BasePage):
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def enter_delay_value(self, value):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def perform_calculation(self, num1, operator, num2):
        self.driver.find_element(By.ID, f"btn_{num1}").click()
        self.driver.find_element(By.ID, f"btn_{operator}").click()
        self.driver.find_element(By.ID, f"btn_{num2}").click()
        self.driver.find_element(By.ID, "btn_equals").click()

    def get_result_after_delay(self, result, delay):
        WebDriverWait(self.driver, delay).until(
            EC.text_to_be_present_in_element((By.ID, "display"), str(result))
        )