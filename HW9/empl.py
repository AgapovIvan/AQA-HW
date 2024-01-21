import requests
from faker import Faker

fake = Faker()

class Company:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(f"{self.url}/auth/login", json=creds)
        return resp.json()["userToken"]

    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/company", json=company, headers=my_headers)
        return resp.json()

    def get_list_employee(self, id):
        my_params = {
            "company": id
        }
        resp = requests.get(f"{self.url}/employee", params=my_params)
        return resp.json()

    def get_employee_by_id(self, id_employee):
        resp = requests.get(f"{self.url}/employee/{id_employee}")
        return resp.json()

    def add_new_employee(self, new_id, name, last_name, email, phone, birthdate):
        employee = {
            "id": fake.random_int(min=1, max=1000),  # Генерация случайного числа для id
            "firstName": name,
            "lastName": last_name,
            "middleName": fake.last_name(),  # Генерация случайной фамилии в качестве отчества
            "companyId": new_id,
            "email": email,
            "url": fake.url(),
            "phone": phone,
            "birthdate": birthdate,
            "isActive": True
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/employee", headers=my_headers, json=employee)
        return resp.json()
    
    def update_employee_info(self, id_employee, last_name, email, is_active=True):
        user_info = {
            "lastName": last_name,
            "email": email,
            "isActive": is_active
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(f"{self.url}/employee/{id_employee}", headers=my_headers, json=user_info)
        return resp.json()
