from celery import Celery
import pytesseract
from sqlalchemy.orm import sessionmaker
from create_tables import engine, DocumentText, Document

# Настройка брокера (RabbitMQ)
celery_app = Celery("tasks", broker="pyamqp://guest@localhost//")

# Настройка сессии базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Путь к исполняемому файлу Tesseract (если требуется)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

@celery_app.task
def analyse_document(doc_id: int):
    # Создаем сессию базы данных
    db = SessionLocal()

    # Получаем документ из базы данных по ID
    document = db.query(Document).filter(Document.id == doc_id).first()
    if not document:
        return f"Document with id {doc_id} not found"

    # Выполняем распознавание текста с помощью Tesseract
    try:
        extracted_text = pytesseract.image_to_string(document.path)
    except Exception as e:
        db.close()
        return f"Error in Tesseract OCR: {str(e)}"

    # Сохраняем результат в таблицу Documents_text
    new_doc_text = DocumentText(id_doc=doc_id, text=extracted_text)
    db.add(new_doc_text)
    db.commit()
    db.close()

    return f"Document {doc_id} analysed successfully and text saved."
