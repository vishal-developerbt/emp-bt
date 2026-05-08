from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Query
from sqlalchemy.orm import Session
import os, uuid

from app.db.database import SessionLocal
from app.models.project_model import Document
from app.schemas.project_schema import DocumentResponse

router = APIRouter()

UPLOAD_DIR = "uploads/documents"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DocumentResponse)
def upload_document(
    file: UploadFile = File(...),
    classification: str = None,
    description: str = None,
    name: str = None,
    process_id: str = None,
    profile_id: str = None,
    sub_process_id: str = None,
    tags: str = None,
    db: Session = Depends(get_db)
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    allowed_types = [
        "application/pdf",
        "image/jpeg",
        "image/png",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(400, "Invalid file type")

    filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = f"{UPLOAD_DIR}/{filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    doc = Document(
        classification=classification,
        description=description,
        name=name,
        document=file_path,
        process_id=process_id,
        profile_id=profile_id,
        sub_process_id=sub_process_id,
        tags=tags
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    return doc

@router.get("/", response_model=list[DocumentResponse])
def get_documents(
    classification: str | None = Query(None),
    process_id: str | None = Query(None),
    profile_id: str | None = Query(None),
    tags: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Document)

    if classification:
        query = query.filter(Document.classification == classification)

    if process_id:
        query = query.filter(Document.process_id == process_id)

    if profile_id:
        query = query.filter(Document.profile_id == profile_id)

    if tags:
        query = query.filter(Document.tags.like(f"%{tags}%"))

    return query.order_by(Document.created_at.desc()).all()


@router.get("/{id}", response_model=DocumentResponse)
def get_document(id: str, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == id).first()

    if not doc:
        raise HTTPException(404, "Document not found")

    return doc

@router.delete("/{id}")
def delete_document(id: str, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == id).first()

    if not doc:
        raise HTTPException(404, "Not found")

    if doc.document and os.path.exists(doc.document):
        os.remove(doc.document)

    db.delete(doc)
    db.commit()

    return {"message": "Deleted successfully"}