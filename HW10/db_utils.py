from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, MetaData, Table  # Add 'Table' here
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("postgresql://x_clients_user:[axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com]/x_clients")
metadata = MetaData()

employee_table = Table(
    'employee', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('is_active', Boolean, nullable=False, default=True),
    Column('create_timestamp', DateTime, server_default=func.now(), nullable=False),
    Column('change_timestamp', DateTime, server_default=func.now(), onupdate=func.now(), nullable=False),
    Column('first_name', String(20), nullable=False),
    Column('last_name', String(20), nullable=False),
    Column('middle_name', String(20)),
    Column('phone', String(15), nullable=False),
    Column('email', String(256)),
    Column('avatar_url', String(1024)),
    Column('company_id', Integer, nullable=False)
)

class Employee(Base):
    __table__ = employee_table

Session = sessionmaker(bind=engine)








