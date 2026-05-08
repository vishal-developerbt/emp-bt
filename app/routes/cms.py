from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.cms_model import CMS
from app.schemas.cms_schema import CMSCreate, CMSUpdate, CMSResponse
from app.core.deps import get_current_user
from app.models.employee_model import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=CMSResponse)
def create_cms(
    data: CMSCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    existing = db.query(CMS).filter(CMS.title == data.title).first()
    if existing:
        raise HTTPException(400, "Page already exists")

    cms = CMS(**data.dict())

    db.add(cms)
    db.commit()
    db.refresh(cms)

    return cms


@router.put("/{id}", response_model=CMSResponse)
def update_cms(
    id: int,
    data: CMSUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    cms = db.query(CMS).filter(CMS.id == id).first()

    if not cms:
        raise HTTPException(404, "Page not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(cms, field, value)

    db.commit()
    db.refresh(cms)

    return cms

@router.delete("/{id}")
def delete_cms(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    cms = db.query(CMS).filter(CMS.id == id).first()

    if not cms:
        raise HTTPException(404, "Page not found")

    db.delete(cms)
    db.commit()

    return {"message": "Deleted successfully"}