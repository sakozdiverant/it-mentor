from pz10_part2 import Client, Supplier, Delivery, Employee, Product, Order
from sqlalchemy import create_engine, update, func, cast, Numeric
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/ITM_alchem"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def update_client_phones():
    stmt = (
        update(Client)
        .where(Client.Телефон.like('+7-900%'))
        .values(Телефон=func.replace(Client.Телефон, '+7-900', '+7-777'))
    )

    session.execute(stmt)
    session.commit()


def update_product_prices():
    stmt = (
        update(Product)
        .values(
            СтоимостьЗакупки=func.round(cast(Product.СтоимостьЗакупки, Numeric) * 1.15, 2),
            СтоимостьПродажи=func.round(cast(Product.СтоимостьПродажи, Numeric) * 1.15, 2)
        )
    )

    session.execute(stmt)
    session.commit()

if __name__ == '__main__':
    update_client_phones()
    update_product_prices()

