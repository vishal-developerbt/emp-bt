from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os

from app.db.database import SessionLocal
from app.models.claim_image import ClaimImage
from app.models.claim import Claim
from app.schemas.claim_image import ClaimImageResponse
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/claim-images", tags=["Claim Images"])


UPLOAD_DIR = "uploads/claims"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{claim_id}", response_model=list[ClaimImageResponse])
def upload_claim_images(
    claim_id: int,
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    claim = db.query(Claim).filter(
        Claim.id == claim_id,
        Claim.user_id == current_user.id
    ).first()

    if not claim:
        raise HTTPException(404, "Claim not found")

    saved_files = []

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    for file in files:
        file_path = f"{UPLOAD_DIR}/{file.filename}"

        with open(file_path, "wb") as f:
            f.write(file.file.read())

        image = ClaimImage(
            claim_id=claim_id,
            file_upload=file_path
        )

        db.add(image)
        saved_files.append(image)

    db.commit()

    for img in saved_files:
        db.refresh(img)

    return saved_files

@router.get("/{claim_id}", response_model=list[ClaimImageResponse])
def get_claim_images(claim_id: int, db: Session = Depends(get_db)):
    return db.query(ClaimImage).filter(
        ClaimImage.claim_id == claim_id
    ).all()