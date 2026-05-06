from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.emp_band import EmpBand
from app.schemas.emp_band import (
    BandCreate,
    BandUpdate,
    BandResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BandResponse)
def create_band(data: BandCreate, db: Session = Depends(get_db)):

    existing = db.query(EmpBand).filter(
        EmpBand.emp_band == data.emp_band
    ).first()

    if existing:
        raise HTTPException(400, "Band already exists")

    band = EmpBand(**data.dict())

    db.add(band)
    db.commit()
    db.refresh(band)

    return band

@router.put("/{id}", response_model=BandResponse)
def update_band(id: int, data: BandUpdate, db: Session = Depends(get_db)):
    band = db.query(EmpBand).filter(EmpBand.id == id).first()

    if not band:
        raise HTTPException(404, "Band not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(band, field, value)

    db.commit()
    db.refresh(band)

    return band



@router.get("/active", response_model=list[BandResponse])
def get_active_bands(db: Session = Depends(get_db)):
    return db.query(EmpBand).filter(
        EmpBand.status == True
    ).all()