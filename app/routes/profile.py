from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid

from app.db.database import SessionLocal
from app.models.profile import Profile
from app.schemas.profile import (
    ProfileCreate,
    ProfileUpdate,
    ProfileResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProfileResponse)
def create_profile(data: ProfileCreate, db: Session = Depends(get_db)):

    profile = Profile(
        id=str(uuid.uuid4()),  # ✅ generate string ID
        **data.dict()
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile

@router.get("/", response_model=list[ProfileResponse])
def get_profiles(db: Session = Depends(get_db)):
    return db.query(Profile).all()

@router.get("/{id}", response_model=ProfileResponse)
def get_profile(id: str, db: Session = Depends(get_db)):
    profile = db.query(Profile).filter(Profile.id == id).first()

    if not profile:
        raise HTTPException(404, "Profile not found")

    return profile

@router.put("/{id}", response_model=ProfileResponse)
def update_profile(id: str, data: ProfileUpdate, db: Session = Depends(get_db)):

    profile = db.query(Profile).filter(Profile.id == id).first()

    if not profile:
        raise HTTPException(404, "Profile not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(profile, field, value)

    db.commit()
    db.refresh(profile)

    return profile

@router.delete("/{id}")
def delete_profile(id: str, db: Session = Depends(get_db)):

    profile = db.query(Profile).filter(Profile.id == id).first()

    if not profile:
        raise HTTPException(404, "Profile not found")

    db.delete(profile)
    db.commit()

    return {"message": "Deleted successfully"}