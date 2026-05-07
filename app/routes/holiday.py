from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.attendance_model import Holiday
from app.schemas.attendance_schema import (
    HolidayCreate,
    HolidayUpdate,
    HolidayResponse
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=HolidayResponse)
def create_holiday(data: HolidayCreate, db: Session = Depends(get_db)):
    new_holiday = Holiday(
        holiday_name=data.holiday_name,
        date=data.date,
        type=data.type,
        status=data.status
    )

    db.add(new_holiday)
    db.commit()
    db.refresh(new_holiday)

    return new_holiday

@router.put("/{id}", response_model=HolidayResponse)
def update_holiday(id: int, data: HolidayUpdate, db: Session = Depends(get_db)):
    holiday = db.query(Holiday).filter(Holiday.id == id).first()

    if not holiday:
        raise HTTPException(status_code=404, detail="Holiday not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(holiday, field, value)

    db.commit()
    db.refresh(holiday)

    return holiday

@router.get("/", response_model=list[HolidayResponse])
def get_all_holidays(db: Session = Depends(get_db)):
    holidays = db.query(Holiday).order_by(Holiday.date.asc()).all()
    return holidays