from pz10_part2 import Client, Supplier, Delivery, Employee, Product, Order
from sqlalchemy import create_engine, func, select, desc, distinct
from sqlalchemy.orm import sessionmaker

# Настройка соединения с базой данных
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/ITM_alchem"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Получение данных с использованием WHERE, ORDER BY, GROUP BY, DISTINCT
def get_product_sales():
    stmt = (
        select(
            Product.НаименованиеТовара,
            func.sum(Product.СтоимостьПродажи).label('общая_сумма')
        )
        .group_by(Product.НаименованиеТовара)
        .having(func.sum(Product.СтоимостьПродажи) > 50000)
    )

    results = session.execute(stmt).fetchall()
    for result in results:
        print(result)

def get_expensiv_buy():
    stmt = (
        select(Product)
        .order_by(desc(Product.СтоимостьЗакупки))
    )

    result = session.execute(stmt)
    products = result.scalars().all()
    for product in products:
        print(product.НаименованиеТовара, product.СтоимостьЗакупки)

def count_unique_products_in_orders():
    stmt = func.count(distinct(Order.КодТовара))

    result = session.query(stmt)
    count = result.scalar()  # Получаем единственное значение
    print(f"Количество уникальных товаров в заказах: {count}")

def need_orders():
    stmt = (
        select(
            Product.НаименованиеТовара,
            Product.Количество
        )
        .where(Product.Количество < 20)
    )

    results = session.execute(stmt).fetchall()
    for result in results:
        print(result)

if __name__ == '__main__':
    get_product_sales()
    get_expensiv_buy()
    count_unique_products_in_orders()
    need_orders()
