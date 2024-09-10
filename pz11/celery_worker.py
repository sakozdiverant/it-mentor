from celery import Celery
import pytesseract
from sqlalchemy.orm import sessionmaker
from create_tables import engine, DocumentText, Document
import logging
import os

logger = logging.getLogger(__name__)

# Настройка брокера (RabbitMQ)
celery_app = Celery(
    'tasks',
    broker='amqp://guest:guest@rabbitmq:5672//',
    backend='rpc://'
)
celery_app.conf.update(
    result_expires=3600,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Путь к исполняемому файлу Tesseract (если требуется)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

@celery_app.task
def analyse_document(doc_id: int):
    db = SessionLocal()
    document = db.query(Document).filter(Document.id == doc_id).first()

    if not document:
        print(f"Document with id {doc_id} not found")
        return f"Document with id {doc_id} not found"

    print(f"Document path: {document.path}")

    # Выполняем распознавание текста с помощью Tesseract
    try:
        extracted_text = pytesseract.image_to_string(document.path)
        print(f"Extracted text: {extracted_text}")
    except Exception as e:
        print(f"Error in Tesseract OCR: {str(e)}")
        db.rollback()  # Откатываем транзакцию, если что-то пошло не так
        db.close()
        return f"Error in Tesseract OCR: {str(e)}"

    try:
        new_doc_text = DocumentText(id_doc=doc_id, text=extracted_text)
        db.add(new_doc_text)
        db.commit()
        print(f"Document {doc_id} analysed successfully and text saved.")
    except Exception as e:
        print(f"Error saving text: {str(e)}")
        db.rollback()  # Откатываем транзакцию, если что-то пошло не так
    finally:
        db.close()

    return f"Document {doc_id} analysed successfully and text saved."

#apt-get update && apt-get install -y tesseract-ocr
#apt-get update && apt-get install -y nano
