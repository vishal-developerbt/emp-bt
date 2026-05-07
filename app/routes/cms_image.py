from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os, uuid

from app.db.database import SessionLocal
from app.models.cms_model import CMSImage
from app.models.cms_model import CMS
from app.schemas.cms_schema import CMSImageResponse
from app.core.deps import get_current_user
from app.models.employee_model import User

router = APIRouter()

UPLOAD_DIR = "uploads/cms"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/{cms_id}", response_model=list[CMSImageResponse])
def upload_cms_images(
    cms_id: int,
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    cms = db.query(CMS).filter(CMS.id == cms_id).first()
    if not cms:
        raise HTTPException(404, "CMS page not found")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    saved = []
    allowed_types = ["image/jpeg", "image/png", "image/webp"]

    for file in files:
        if file.content_type not in allowed_types:
            raise HTTPException(400, "Invalid file type")

        filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = f"{UPLOAD_DIR}/{filename}"

        with open(file_path, "wb") as f:
            f.write(file.file.read())

        img = CMSImage(
            cms_id=cms_id,
            file_name=file_path
        )

        db.add(img)
        saved.append(img)

    db.commit()

    for img in saved:
        db.refresh(img)

    return saved

@router.get("/{cms_id}", response_model=list[CMSImageResponse])
def get_cms_images(cms_id: int, db: Session = Depends(get_db)):
    return db.query(CMSImage).filter(
        CMSImage.cms_id == cms_id,
        CMSImage.status == True
    ).all()

