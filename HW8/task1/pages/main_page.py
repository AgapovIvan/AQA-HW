from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def text_name(self, ):
        fields = {
            0: ["[name='first-name']", "Иван"],
            1: ["[name='last-name']", "Петров"],
            2: ["[name='address']", "Ленина, 55-3"],
            3: ["[name='zip-code']", ""],
            4: ["[name='city']", "Москва"],
            5: ["[name='country']", "Россия"],
            6: ["[name='e-mail']", "test@mail.ru"],
            7: ["[name='phone']", "89922211199"],
            8: ["[name='job-position']", "QA"],
            9: ["[name='company']", "SkyPro"]

        }
        for i in range(len(fields)):
            self._driver.find_element(By.CSS_SELECTOR, fields[i][0]).send_keys(fields[i][1])

    def button(self, locator: str):
        self._driver.find_element(By.CSS_SELECTOR, locator).click()

    def first_name(self):
        first_name = self._driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
        return first_name

    def last_name(self):
        last_name = self._driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color")
        return last_name

    def address(self):
        address = self._driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color")
        return address

    def zip_code(self):
        zip_code = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return zip_code

    def city(self):
        city = self._driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color")
        return city

    def country(self):
        country = self._driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color")
        return country

    def e_mail(self):
        e_mail = self._driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")
        return e_mail

    def phone(self):
        phone = self._driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")
        return phone

    def job_position(self):
        job_position = self._driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color")
        return job_position

    def company(self):
        company = self._driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color")
        return company
        green_highlighted_fields = self.driver.find_elements(By.CSS_SELECTOR, "div.alert.py-2.alert-success")
        return len(green_highlighted_fields) == 9