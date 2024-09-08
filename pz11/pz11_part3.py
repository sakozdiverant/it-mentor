from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date
from fastapi.responses import JSONResponse
from create_tables import SessionLocal, Document
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