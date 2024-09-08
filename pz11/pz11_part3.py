from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date
from fastapi.responses import JSONResponse
from create_tables import SessionLocal, Document, DocumentText
from celery_worker import analyse_document
import os
import base64

app = FastAPI()

document_path = "documents"
if not os.path.exists(document_path):
    os.makedirs(document_path)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class DocumentUpload(BaseModel):
    filename: str
    file_data: str



@app.post("/upload_doc/")
def upload_document(doc: DocumentUpload, db: Session = Depends(get_db)):
    try:
        file_data = base64.b64decode(doc.file_data)
        file_path = os.path.join(document_path, doc.filename)
        with open(file_path, "wb") as file:
            file.write(file_data)

        # Создание записи в базе данных
        new_doc = Document(path=file_path, date=date.today())
        db.add(new_doc)
        db.commit()
        db.refresh(new_doc)

        return {"id": new_doc.id, "path": new_doc.path, "date": new_doc.date}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@app.delete("/doc_delete/{doc_id}")
def delete_document(doc_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == doc_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    file_path = document.path
    db.delete(document)
    db.commit()

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting file: {str(e)}")

    return JSONResponse(content={"message": "Document and file successfully deleted"})


@app.post("/doc_analyse/{doc_id}")
def analyse_document_api(doc_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == doc_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    # Вызываем задачу в Celery
    analyse_document(doc_id)

    return {"message": f"Document {doc_id} is being analysed."}

@app.get("/get_text/{doc_id}")
def get_document_text(doc_id: int, db: Session = Depends(get_db)):
    document_text = db.query(DocumentText).filter(DocumentText.id_doc == doc_id).first()

    if not document_text:
        raise HTTPException(status_code=404, detail="Text for the document not found")
    return {"document_id": doc_id, "text": document_text.text}

#Satrt rabbitmq-server.bat
#Satrt celery -A celery_worker.celery_app worker --loglevel=info
#venv\Scripts\activate
#Start uvicorn pz11_part3:app --reload


