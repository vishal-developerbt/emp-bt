from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.technology import Technology
from app.schemas.technology import (
    TechnologyCreate,
    TechnologyUpdate,
    TechnologyResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TechnologyResponse)
def create_technology(data: TechnologyCreate, db: Session = Depends(get_db)):
    new_tech = Technology(
        technology=data.technology,
        status=data.status
    )

    db.add(new_tech)
    db.commit()
    db.refresh(new_tech)

    return new_tech

@router.put("/{tech_id}", response_model=TechnologyResponse)
def update_technology(tech_id: int, data: TechnologyUpdate, db: Session = Depends(get_db)):
    tech = db.query(Technology).filter(Technology.id == tech_id).first()

    if not tech:
        raise HTTPException(status_code=404, detail="Technology not found")

    if data.technology is not None:
        tech.technology = data.technology

    if data.status is not None:
        tech.status = data.status

    db.commit()
    db.refresh(tech)

    return tech

@router.delete("/{tech_id}")
def delete_technology(tech_id: int, db: Session = Depends(get_db)):
    tech = db.query(Technology).filter(Technology.id == tech_id).first()

    if not tech:
        raise HTTPException(status_code=404, detail="Technology not found")

    db.delete(tech)
    db.commit()

    return {"message": "Technology deleted successfully"}