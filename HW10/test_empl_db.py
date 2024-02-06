from empl import Company
from EmplTable import EmplTable
import pytest

api = Company("https://x-clients-be.onrender.com")
db = EmplTable("postgresql://x_clients_user:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com:5432/x_clients")


def setup_module(module):
    db.create_table()


def teardown_module(module):
    db.__db.dispose()


def test_create_and_get_employee():
    name = "SkyPro"
    descr = "testing"
    company = api.create_company(name, descr)
    new_company_id = company["id"]

    len_before = len(db.get_employees())

    db.insert_employee("Mike", "Sorreto", "+123456789", new_company_id)

    len_after = len(db.get_employees())

    assert len_after - len_before == 1

    employee_list = api.get_list_employee(new_company_id)
    assert any(employee["firstName"] == "Mike" and employee["lastName"] == "Sorreto" for employee in employee_list)


def test_update_employee():
    name = "SkyPro"
    descr = "testing"
    company = api.create_company(name, descr)
    new_id = company["id"]

    db.insert_employee("Jane", "Doe", "+123456789", new_id)

    employees = db.get_employees()
    assert len(employees) > 0

    employee_id = employees[0]["id"]
    db.update_employee(employee_id, "Jane", "Doe", "Middle", "+987654321", "jane.doe@example.com", "http://example.com")

    updated_employee = db.get_employees()[0]
    assert updated_employee["first_name"] == "Jane"
    assert updated_employee["last_name"] == "Doe"
    assert updated_employee["middle_name"] == "Middle"
    assert updated_employee["phone"] == "+987654321"
    assert updated_employee["email"] == "jane.doe@example.com"
    assert updated_employee["avatar_url"] == "http://example.com"


def test_delete_employee():
    name = "SkyPro"
    descr = "testing"
    company = api.create_company(name, descr)
    new_id = company["id"]

    db.insert_employee("John", "Doe", "+123456789", new_id)

    len_before = len(db.get_employees())

    employees = db.get_employees()

    employee_id = employees[0]["id"]
    db.delete_employee(employee_id)

    len_after = len(db.get_employees())

    assert len_before - len_after == 1
