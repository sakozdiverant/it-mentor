from celery import Celery
import pytesseract
from sqlalchemy.orm import sessionmaker
from create_tables import engine, DocumentText, Document
import logging
import os

logger = logging.getLogger(__name__)

# Настройка брокера (RabbitMQ)
broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
celery_app = Celery("tasks", broker=broker_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Путь к исполняемому файлу Tesseract (если требуется)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

@celery_app.task
def analyse_document(doc_id: int):
    db = SessionLocal()
    document = db.query(Document).filter(Document.id == doc_id).first()
    if not document:
        return f"Document with id {doc_id} not found"

    # Выполняем распознавание текста с помощью Tesseract
    try:
        extracted_text = pytesseract.image_to_string(document.path)
    except Exception as e:
        db.close()
        return f"Error in Tesseract OCR: {str(e)}"

    new_doc_text = DocumentText(id_doc=doc_id, text=extracted_text)
    db.add(new_doc_text)
    db.commit()
    db.close()

    return f"Document {doc_id} analysed successfully and text saved."
