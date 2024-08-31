from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Client(Base):
    __tablename__ = "Клиенты"
    Код = Column(Integer, primary_key=True, nullable=False)
    ФИО = Column(String(255), nullable=False)
    Адрес = Column(Text, nullable=False)
    Телефон = Column(String(15), nullable=False)
    orders = relationship("Order", back_populates="client")


class Supplier(Base):
    __tablename__ = "Поставщик"
    КодПоставщика = Column(Integer, primary_key=True, nullable=False)
    НазваниеПоставщика = Column(String(100), nullable=False)
    ПредставительПоставщика = Column(String(100))
    Обращаться = Column(String(100), nullable=False)
    КонтактныйТелефон = Column(String(100), nullable=False)
    Адрес = Column(Text)
    deliveries = relationship("Delivery", back_populates="supplier")


class Delivery(Base):
    __tablename__ = "Поставка"
    КодПоставки = Column(Integer, primary_key=True, nullable=False)
    КодПоставщика = Column(Integer, ForeignKey("Поставщик.КодПоставщика"), nullable=False)
    ДатаПоставки = Column(Date)
    supplier = relationship("Supplier", back_populates="deliveries")
    goods = relationship("Product", back_populates="delivery")


class Employee(Base):
    __tablename__ = "Сотрудники"
    КодСотрудника = Column(Integer, primary_key=True, nullable=False)
    Фамилия = Column(String(100), nullable=False)
    Имя = Column(String(100), nullable=False)
    Отчество = Column(String(100))
    Должность = Column(String(100), nullable=False)
    Адрес = Column(Text)
    ДомашнийТелефон = Column(String(15))
    ДатаРождения = Column(Date)
    orders = relationship("Order", back_populates="employee")


class Product(Base):
    __tablename__ = "Товары"
    КодТовара = Column(Integer, primary_key=True, nullable=False)
    КодПоставки = Column(Integer, ForeignKey("Поставка.КодПоставки"), nullable=False)
    НаименованиеТовара = Column(String(100), nullable=False)
    ТехническиеХарактеристики = Column(String(100), nullable=False)
    Описание = Column(String(100), nullable=False)
    Изображение = Column(Text)
    СтоимостьЗакупки = Column(String(15), nullable=False)
    Наличие = Column(String(3), nullable=False)
    Количество = Column(Integer, nullable=False)
    СтоимостьПродажи = Column(Integer, nullable=False)
    delivery = relationship("Delivery", back_populates="goods")
    orders = relationship("Order", back_populates="product")


class Order(Base):
    __tablename__ = "Заказы"
    КодЗаказа = Column(Integer, primary_key=True, nullable=False)
    КодСотрудника = Column(Integer, ForeignKey("Сотрудники.КодСотрудника"), nullable=False)
    КодТовара = Column(Integer, ForeignKey("Товары.КодТовара"), nullable=False)
    ДатаРазмещения = Column(Date, nullable=False)
    ДатаИсполнения = Column(Date)
    КодКлиента = Column(Integer, ForeignKey("Клиенты.Код"), nullable=False)
    employee = relationship("Employee", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    client = relationship("Client", back_populates="orders")

def make_tables(bd_post='ITM_alchem'):
    DATABASE_URL = f"postgresql+psycopg2://postgres:admin@localhost:5432/{bd_post}"
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    make_tables()