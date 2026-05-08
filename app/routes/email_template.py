from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.cms_model import EmailTemplate
from app.schemas.cms_schema import (
    EmailTemplateCreate,
    EmailTemplateUpdate,
    EmailTemplateResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EmailTemplateResponse)
def create_template(data: EmailTemplateCreate, db: Session = Depends(get_db)):

    existing = db.query(EmailTemplate).filter(
        EmailTemplate.type == data.type
    ).first()

    if existing:
        raise HTTPException(400, "Template type already exists")

    template = EmailTemplate(**data.dict())

    db.add(template)
    db.commit()
    db.refresh(template)

    return template

@router.put("/{id}", response_model=EmailTemplateResponse)
def update_template(id: int, data: EmailTemplateUpdate, db: Session = Depends(get_db)):
    template = db.query(EmailTemplate).filter(EmailTemplate.id == id).first()

    if not template:
        raise HTTPException(404, "Template not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(template, field, value)

    db.commit()
    db.refresh(template)

    return template


@router.delete("/{id}")
def delete_template(id: int, db: Session = Depends(get_db)):
    template = db.query(EmailTemplate).filter(EmailTemplate.id == id).first()

    if not template:
        raise HTTPException(404, "Template not found")

    db.delete(template)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/type/{type}", response_model=EmailTemplateResponse)
def get_template_by_type(type: str, db: Session = Depends(get_db)):
    template = db.query(EmailTemplate).filter(
        EmailTemplate.type == type,
        EmailTemplate.status == True
    ).first()

    if not template:
        raise HTTPException(404, "Template not found")

    return template