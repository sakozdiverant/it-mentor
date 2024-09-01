from pz10_part2 import Client, Supplier, Delivery, Employee, Product, Order
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, delete, text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Настройка соединения с базой данных
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/ITM_alchem"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def delete_supplier():
    stmt_delete = delete(Supplier).where(Supplier.КодПоставщика > 208)
    session.execute(stmt_delete)
    session.commit()

    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        print(f"{supplier.КодПоставщика}, {supplier.Обращаться}, {supplier.НазваниеПоставщика}")


if __name__ == '__main__':
    delete_supplier()
