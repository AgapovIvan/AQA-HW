import pytest
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, Session



# Ваш код ...

# Определение схемы базы данных
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, nullable=False, default=True)
    create_timestamp = Column(DateTime, nullable=False, server_default='now()')
    change_timestamp = Column(DateTime, nullable=False, server_default='now()')
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    middle_name = Column(String(20))
    phone = Column(String(15), nullable=False)
    email = Column(String(256))
    avatar_url = Column(String(1024))
    company_id = Column(Integer, nullable=False)

# Методы для работы с базой данных
class TestEmployeeDB:

    @pytest.fixture
    def db_session(self):
        # Строка подключения к БД
        db_url = "postgresql://x_clients_user:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com:5432/x_clients"
        # Создание соединения с БД
        engine = create_engine(db_url)
        # Создание сессии для работы с БД
        session = Session(engine)
        
        # Создание таблицы, если ее нет
        if not engine.dialect.has_table(engine, "employee"):
            Base.metadata.create_all(engine)
        
        return session

    def create_employee(self, session, first_name, last_name, phone, company_id):
        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            company_id=company_id
        )
        session.add(employee)
        session.commit()
        return employee.id

    def delete_employee(self, session, employee_id):
        employee = session.query(Employee).get(employee_id)
        if employee:
            session.delete(employee)
            session.commit()

    def test_create_and_delete_employee(self, db_session: Session):
        company_id = 1  # ID компании, полученный из тестов
        employee_id = self.create_employee(db_session, "John", "Doe", "123456789", company_id)
        assert employee_id is not None

        # Проверяем, что сотрудник успешно создан
        employee = db_session.query(Employee).get(employee_id)
        assert employee is not None

        # Удаляем сотрудника
        self.delete_employee(db_session, employee_id)

        # Проверяем, что сотрудник успешно удален
        employee = db_session.query(Employee).get(employee_id)
        assert employee is None
