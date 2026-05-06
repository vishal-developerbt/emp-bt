from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.city_state import CityState
from app.schemas.city_state import CityStateCreate, CityStateResponse

router = APIRouter(prefix="/city-states", tags=["City States"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CityStateResponse)
def create_city_state(data: CityStateCreate, db: Session = Depends(get_db)):
    existing = db.query(CityState).filter(
        CityState.state == data.state,
        CityState.city == data.city
    ).first()

    if existing:
        raise HTTPException(400, "City already exists in this state")

    record = CityState(**data.dict())

    db.add(record)
    db.commit()
    db.refresh(record)

    return record

@router.get("/", response_model=list[CityStateResponse])
def get_all(db: Session = Depends(get_db)):
    return db.query(CityState).order_by(CityState.state).all()

@router.get("/by-state", response_model=list[CityStateResponse])
def get_by_state(state: str = Query(...), db: Session = Depends(get_db)):
    return db.query(CityState).filter(
        CityState.state == state
    ).all()

@router.delete("/{id}")
def delete_city_state(id: int, db: Session = Depends(get_db)):
    record = db.query(CityState).filter(CityState.id == id).first()

    if not record:
        raise HTTPException(404, "Not found")

    db.delete(record)
    db.commit()

    return {"message": "Deleted successfully"}