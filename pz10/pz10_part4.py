# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect
from pz10_part2 import Client, Supplier, Delivery, Employee, Product, Order

bd_post='321'
DATABASE_URL = f"postgresql+psycopg2://postgres:admin@localhost:5432/{bd_post}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

inspector = inspect(engine)
tables = inspector.get_table_names()

products = session.query(Product).all()
for product in products:
    print(f"{product.НаименованиеТовара}, Стоимость = {product.СтоимостьПродажи}")

clients = session.query(Client).all()
for client in clients:
    print(f"{client.ФИО}, {client.Адрес}, {client.Телефон}")

session.close()
