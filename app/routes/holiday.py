from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.holiday import Holiday
from app.schemas.holiday import HolidayCreate, HolidayResponse
from app.models.user import User
from app.core.deps import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Add Holiday (Admin)
@router.post("/", response_model=HolidayResponse)
def create_holiday(
    data: HolidayCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    holiday = Holiday(**data.dict())

    db.add(holiday)
    db.commit()
    db.refresh(holiday)

    return holiday


# Get All Holidays
@router.get("/", response_model=list[HolidayResponse])
def get_holidays(db: Session = Depends(get_db)):
    return db.query(Holiday).order_by(Holiday.date).all()

@router.get("/{id}", response_model=HolidayResponse)
def get_holiday_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    holiday = db.query(Holiday).filter(Holiday.id == id).first()

    if not holiday:
        raise HTTPException(status_code=404, detail="Holiday not found")

    return holiday

@router.put("/{id}", response_model=HolidayResponse)
def update_holiday(
    id: int,
    data: HolidayCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    holiday = db.query(Holiday).filter(Holiday.id == id).first()

    if not holiday:
        raise HTTPException(status_code=404, detail="Holiday not found")

    # Update fields
    for key, value in data.dict().items():
        setattr(holiday, key, value)

    db.commit()
    db.refresh(holiday)

    return holiday

@router.delete("/{id}")
def delete_holiday(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    holiday = db.query(Holiday).filter(Holiday.id == id).first()

    if not holiday:
        raise HTTPException(status_code=404, detail="Holiday not found")

    db.delete(holiday)
    db.commit()

    return {"message": "Holiday deleted successfully"}