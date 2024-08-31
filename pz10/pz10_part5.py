# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect
from pz10_part2 import Client, Supplier, Delivery, Employee, Product, Order

# Создаем движок и сессию

bd_post='ITM_alchem'
DATABASE_URL = f"postgresql+psycopg2://postgres:admin@localhost:5432/{bd_post}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def query_orders_with_clients_and_products():
    results = session.query(Order, Client, Product).\
        join(Client, Order.КодКлиента == Client.Код).\
        join(Product, Order.КодТовара == Product.КодТовара).\
        all()

    for order, client, product in results:
        print(f"КодЗаказа: {order.КодЗаказа}, Client ФИО: {client.ФИО}, Товар: {product.НаименованиеТовара}, "
              f"Order Date: {order.ДатаРазмещения}")

def query_products_with_deliveries_and_suppliers():
    results = session.query(Product, Delivery, Supplier).\
        join(Delivery, Product.КодПоставки == Delivery.КодПоставки).\
        join(Supplier, Delivery.КодПоставщика == Supplier.КодПоставщика).\
        all()

    for product, delivery, supplier in results:
        print(f"Товар: {product.НаименованиеТовара}, Дата Поставки: {delivery.ДатаПоставки}, "
              f"Поставщик: {supplier.НазваниеПоставщика}")

def query_orders_with_employees_clients_and_products():
    results = session.query(Order, Employee, Client, Product).\
        join(Employee, Order.КодСотрудника == Employee.КодСотрудника).\
        join(Client, Order.КодКлиента == Client.Код).\
        join(Product, Order.КодТовара == Product.КодТовара).\
        all()

    for order, employee, client, product in results:
        print(f"Код Заказа: {order.КодЗаказа}, Продовец: {employee.Фамилия} {employee.Имя}, Клент: {client.ФИО}, "
              f"Товар: {product.НаименованиеТовара}, Дата Размещения: {order.ДатаРазмещения}")

if __name__ == '__main__':
    print("Получение всех заказов с данными о клиентах и товарах")
    query_orders_with_clients_and_products()

    print("\nПолучение всех товаров с данными о поставках и поставщиках")
    query_products_with_deliveries_and_suppliers()

    print("\nПолучение всех заказов с данными о сотрудниках, клиентах и товарах")
    query_orders_with_employees_clients_and_products()