from pz10_part2 import Client, Supplier, Delivery, Employee, Product, Order
from sqlalchemy import create_engine, func, select, desc, distinct
from sqlalchemy.orm import sessionmaker

# Настройка соединения с базой данных
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/ITM_alchem"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

#SUM с GROUP BY: Суммирование значений по группам.
def aggregate_SUM():
    stmt = (
        select(
            Product.НаименованиеТовара,
            func.sum(Product.СтоимостьПродажи)
        )
        .group_by(Product.НаименованиеТовара)

    )
    results = session.execute(stmt).fetchall()
    for result in results:
        print(result)

#AVG с GROUP BY: Среднее значение по группам.
def aggregate_AVG():
    stmt = (
        select(
            Product.НаименованиеТовара,
            func.avg(Product.СтоимостьПродажи)
        )
        .group_by(Product.НаименованиеТовара)

    )
    results = session.execute(stmt).fetchall()
    for result in results:
        print(result)

#MIN с GROUP BY: Минимальное значение по группам.
def aggregate_MIN():
    stmt = (
        select(
            Delivery.КодПоставщика,
            func.min(Delivery.ДатаПоставки)
        )
        .group_by(Delivery.КодПоставщика)

    )
    results = session.execute(stmt).fetchall()
    for result in results:
        print(result)

if __name__ == '__main__':
    #aggregate_SUM()
    #aggregate_AVG()
    aggregate_MIN()
