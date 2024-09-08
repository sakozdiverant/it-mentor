# -*- coding: utf-8 -*-
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date
from create_tables import SessionLocal, Document, DocumentText
from celery import Celery
import pytesseract
from sqlalchemy.orm import sessionmaker
from create_tables import engine, DocumentText, Document

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DocumentCreate(BaseModel):
    path: str
    date: date


class DocumentTextCreate(BaseModel):
    id_doc: int
    text: str


@app.post("/documents")
def create_document(doc: DocumentCreate, db: Session = Depends(get_db)):
    new_doc = Document(path=doc.path, date=doc.date)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc


@app.post("/documents_text")
def create_document_text(doc_text: DocumentTextCreate, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == doc_text.id_doc).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    new_doc_text = DocumentText(id_doc=doc_text.id_doc, text=doc_text.text)
    db.add(new_doc_text)
    db.commit()
    db.refresh(new_doc_text)
    return new_doc_text
