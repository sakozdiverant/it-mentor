# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from path_bd import path_bd
import os


#DATABASE_URL = path_bd
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:admin@postgres_db:5432/FastAPI_ITM')
engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    texts = relationship("DocumentText", back_populates="document")


class DocumentText(Base):
    __tablename__ = "documents_text"
    id = Column(Integer, primary_key=True, index=True)
    id_doc = Column(Integer, ForeignKey("documents.id"), nullable=False)
    text = Column(String, nullable=False)
    document = relationship("Document", back_populates="texts")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    create_tables()
