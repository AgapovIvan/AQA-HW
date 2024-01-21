from empl import Company
from faker import Faker

fake = Faker()


api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "SkyPro"
    descr = "testing"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0


def test_add_new_employee():
    name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()
    birthdate = fake.date_of_birth().isoformat()
    
    company = api.create_company("SkyPro", "testing")
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, name, last_name, email, phone, birthdate)
    
    assert new_employee["id"] > 0

    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == name
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == last_name


def test_get_employee_by_id():
    name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()
    birthdate = fake.date_of_birth().isoformat()

    company = api.create_company("SkyPro", "testing")
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, name, last_name, email, phone, birthdate)
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    
    assert get_info["firstName"] == name
    assert get_info["lastName"] == last_name


def test_change_employee_info():
    name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()
    birthdate = fake.date_of_birth().isoformat()

    company = api.create_company("SkyPro", "testing")
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, name, last_name, email, phone, birthdate)
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, last_name, email)
    
    assert update["id"] == id_employee
    assert update["email"] == email
    assert update["isActive"] == True
