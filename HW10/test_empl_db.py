from empl import Company
from EmplTable import EmplTable
import pytest

api = Company("https://x-clients-be.onrender.com")
db = EmplTable("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")


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
    
    employees = db.get_employees()
    assert len(employees) > 0

    employee_id = employees[0]["id"]
    db.update_employee(employee_id, "Jane", "Doe", "Middle", "+987654321", "jane.doe@example.com", "http://example.com")

    updated_employee = db.get_employees()
    assert updated_employee[-1]["first_name"] == "Jane"
    assert updated_employee[-1]["last_name"] == "Doe"
    assert updated_employee[-1]["middle_name"] == "Middle"
    assert updated_employee[-1]["phone"] == "+987654321"
    assert updated_employee[-1]["email"] == "jane.doe@example.com"
    assert updated_employee[-1]["avatar_url"] == "http://example.com"


def test_delete_all_employees():

    employees = db.get_employees()

    for employee in employees:
        employee_id = employee["id"]
        db.delete_employee(employee_id)

    employees_after_deletion = db.get_employees()
    assert len(employees_after_deletion) == 0

