import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

def make_bd(bd_post='ITM_alchem'):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    conn.autocommit = True  # Включаем autocommit для выполнения CREATE DATABASE

    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(bd_post)
        ))
        print(f"База данных '{bd_post}' успешно создана!")

    conn.close()


def check_bd(bd_post='ITM_alchem'):
    DATABASE_URL = f"postgresql+psycopg2://postgres:admin@localhost:5432/{bd_post}"
    engine = create_engine(DATABASE_URL)
    Base = declarative_base()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    print(f"База данных {bd_post} успешно Ппроверена!")

if __name__ == "__main__":
    make_bd("321")
    check_bd("321")



