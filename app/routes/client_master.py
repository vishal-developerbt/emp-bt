from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.project_model import ClientMaster
from app.schemas.project_schema import (
    ClientCreate,
    ClientUpdate,
    ClientResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.put("/{id}", response_model=ClientResponse)
def update_client(id: int, data: ClientUpdate, db: Session = Depends(get_db)):
    client = db.query(ClientMaster).filter(ClientMaster.id == id).first()

    if not client:
        raise HTTPException(404, "Client not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(client, field, value)

    db.commit()
    db.refresh(client)

    return client


@router.get("/", response_model=list[ClientResponse])
def get_clients(
    company: str | None = Query(None),
    status: str | None = Query(None),
    technology: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(ClientMaster)

    if company:
        query = query.filter(ClientMaster.company.ilike(f"%{company}%"))

    if status:
        query = query.filter(ClientMaster.status.ilike(f"%{status}%"))

    if technology:
        query = query.filter(ClientMaster.technology.ilike(f"%{technology}%"))

    return query.order_by(ClientMaster.id.desc()).all()


@router.get("/{id}", response_model=ClientResponse)
def get_client(id: int, db: Session = Depends(get_db)):
    client = db.query(ClientMaster).filter(ClientMaster.id == id).first()

    if not client:
        raise HTTPException(404, "Client not found")

    return client


@router.delete("/{id}")
def delete_client(id: int, db: Session = Depends(get_db)):
    client = db.query(ClientMaster).filter(ClientMaster.id == id).first()

    if not client:
        raise HTTPException(404, "Client not found")

    db.delete(client)
    db.commit()

    return {"message": "Deleted successfully"}